from csv2json import convert, load_csv, save_json
import json
import pytest
from os import listdir

csv_file_directory = './TestData/TestFiles/'
expected_output_directory = './TestData/ExpectedOutput/'
converter_directory = './TestData/Converter/'

test_csv_files_path = listdir(csv_file_directory)
test_expected_output_path = listdir(expected_output_directory)


empty_header_tests = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test37', 'test38', 'test39', 'test40', 'test41', 'test42', 'test55', 'test56', 'test57', 'test58', 'test59', 'test60']

sorted_tests = ['test1', 'test2', 'test7', 'test8', 'test13', 'test14', 'test19', 'test20', 'test25', 'test26', 'test37', 'test38', 'test43', 'test44', 'test49', 'test50','test55', 'test56', 'test61', 'test62', 'test67', 'test68']

def converter_file_name(file_name):
    return converter_directory + file_name + 'converter' + '.json'

def file_name_without_extension(file_name):
    return file_name.split('.')[0]

# create all the converted json files inside Converter directory
def create_converter_files():
    for file in test_csv_files_path:
        file_name = file_name_without_extension(file)
        csv_file = csv_file_directory + file
        new_file = converter_file_name(file_name)
        with open(csv_file) as r, open(new_file, 'w') as w:
            try:
                if file_name in empty_header_tests and file_name in sorted_tests:
                    convert(r, w, custom_headers=[], sort_keys=True)
                    print(f"Converted {csv_file} to {new_file} with sort & empty headers")
                elif file_name in empty_header_tests:
                    convert(r, w, custom_headers=[])
                    print(f"Converted {csv_file} to {new_file} with empty headers")
                elif file_name in sorted_tests:
                    convert(r, w, sort_keys=True)
                    print(f"Converted {csv_file} to {new_file} sorted")
                else:
                    convert(r, w)
                    print(f"Converted {csv_file} to {new_file}")
            except Exception as e:
                print(f"Sorting failed for {file_name}", e)


# generate tuples of pairs for json files (input, output)
def generate_pairs():
    pairs = []
    for file in test_expected_output_path:
        file_name = file_name_without_extension(file)
        expected_file = expected_output_directory + file
        converted_file = converter_file_name(file_name)
        pairs.append((converted_file, expected_file))
    return pairs

@pytest.mark.parametrize("test_input, expected", generate_pairs())
def test_json_files(test_input, expected):
    with open(test_input, 'r') as j1, open(expected, 'r') as j2:
        assert json.load(j1) == json.load(j2)


if __name__ == "__main__":
    create_converter_files()


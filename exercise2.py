from csv2json import convert, load_csv, save_json
import json
import pytest
from os import listdir

csv_file_directory = './TestData/TestFiles/'
expected_output_directory = './TestData/ExpectedOutput/'
converter_directory = './TestData/Converter/'

test_csv_files_path = listdir(csv_file_directory)
test_expected_output_path = listdir(expected_output_directory)



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
            convert(r, w)
            print(f"Converted {csv_file} to {new_file}")


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


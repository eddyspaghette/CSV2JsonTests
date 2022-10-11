## Steps to run the test suite


Install pip requirements (in a venv preferably)
```python
pip3 install -r requirements.txt
```

Generate the JSON files from the converter
```python
python3 exercise2.py
```

Run the test or save it to a log file
```python
pytest exercise2.py
```

OR

```python
pytest exercise2.py > log.txt
```

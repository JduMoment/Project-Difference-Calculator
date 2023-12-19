import json

def gendiff_test_file(text, file_name):
    with open(f"gendiff/tests/fixtures/{file_name}.json", 'w') as file:
        json.dump(text, file)

gendiff_test_file({
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
          }, 'file1')


gendiff_test_file({
            "timeout": 20,
            "host": "hexlet.io",
            "verbose": True
          }, 'file2')

gendiff_test_file({}, 'file3')

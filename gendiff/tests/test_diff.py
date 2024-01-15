from gendiff.construct_diff import construct_diff
from gendiff.file_to_dict import transform_to_dict
from gendiff.generate_stylish_lines import generate_stylish_lines


import json


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()

diff_expected_nested = [{'key': 'common', 'value': [{'key': 'follow', 'value': False, 'changes': 'IN_SECOND'}, {'key': 'setting1', 'value': 'Value 1', 'changes': 'SAME'}, {'key': 'setting2', 'value': 200, 'changes': 'IN_FIRST'}, {'key': 'setting3', 'old_value': True, 'new_value': None, 'changes': 'CHANGED'}, {'key': 'setting4', 'value': 'blah blah', 'changes': 'IN_SECOND'}, {'key': 'setting5', 'value': {'key5': 'value5'}, 'changes': 'IN_SECOND'}, {'key': 'setting6', 'value': [{'key': 'doge', 'value': [{'key': 'wow', 'old_value': '', 'new_value': 'so much', 'changes': 'CHANGED'}], 'changes': 'CHANGED'}, {'key': 'key', 'value': 'value', 'changes': 'SAME'}, {'key': 'ops', 'value': 'vops', 'changes': 'IN_SECOND'}], 'changes': 'CHANGED'}], 'changes': 'CHANGED'}, {'key': 'group1', 'value': [{'key': 'baz', 'old_value': 'bas', 'new_value': 'bars', 'changes': 'CHANGED'}, {'key': 'foo', 'value': 'bar', 'changes': 'SAME'}, {'key': 'nest', 'old_value': {'key': 'value'}, 'new_value': 'str', 'changes': 'CHANGED'}], 'changes': 'CHANGED'}, {'key': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}, 'changes': 'IN_FIRST'}, {'key': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}, 'changes': 'IN_SECOND'}]
diff_expected_flat = [{'key': 'follow', 'value': False, 'changes': 'IN_FIRST'}, {'key': 'host', 'value': 'hexlet.io', 'changes': 'SAME'}, {'key': 'proxy', 'value': '123.234.53.22', 'changes': 'IN_FIRST'}, {'key': 'timeout', 'old_value': 50, 'new_value': 20, 'changes': 'CHANGED'}, {'key': 'verbose', 'value': True, 'changes': 'IN_SECOND'}]


def test_construct_diff():
    file1, file2 = transform_to_dict('gendiff/tests/fixtures/file4_for_test.json',
                                     'gendiff/tests/fixtures/file5_for_test.json')
    file3, file4 = transform_to_dict('gendiff/tests/fixtures/file1_for_test.yml',
                                     'gendiff/tests/fixtures/file2_for_test.yml')
    assert construct_diff(file1, file2) == diff_expected_nested
    assert construct_diff(file3, file4) == diff_expected_flat

def test_generate_stylish_lines():
    verif_flat = read_file('gendiff/tests/fixtures/test_expected_flat_stylish.txt')
    assert generate_stylish_lines(diff_expected_flat) == verif_flat


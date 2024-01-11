from gendiff.generate_stylish_lines import generate_stylish_lines
from gendiff.generate_json_file import python_to_json
from gendiff.generate_plain_lines import generate_plain_lines
from gendiff.file_to_dict import transform_to_dict

import json


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()


def test_flat_file():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.json',
        'gendiff/tests/fixtures/file2_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.yml',
        'gendiff/tests/fixtures/file2_for_test.yml')
    verif_stylish = read_file('gendiff/tests/fixtures/test_expected_flat_stylish.txt')
    verif_plain = read_file('gendiff/tests/fixtures/test_expected_flat_plain.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif_stylish
    assert generate_plain_lines(f1_yml, f2_yml) == verif_plain

def test_empty_files():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file3_for_test.json',
        'gendiff/tests/fixtures/file3_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file3_for_test.yml',
        'gendiff/tests/fixtures/file3_for_test.yml')
    verif = read_file('gendiff/tests/fixtures/text_expected_empty_files.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif
    assert generate_plain_lines(f1_yml, f2_yml) == verif

def test_nested_files():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.json',
        'gendiff/tests/fixtures/file5_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.yml',
        'gendiff/tests/fixtures/file5_for_test.yml')
    verif_stylish = read_file('gendiff/tests/fixtures/test_expected_nested_stylish.txt')
    verif_plain = read_file('gendiff/tests/fixtures/test_expected_nested_plain.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif_stylish
    assert generate_plain_lines(f2_yml, f2_yml) == verif_plain

def test_diff_to_json():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.json',
        'gendiff/tests/fixtures/file5_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.yml',
        'gendiff/tests/fixtures/file5_for_test.yml')
    open_json = open('gendiff/tests/fixtures/test_diff_to_json.json')
    verif = json.load(verif)
    assert python_to_json(f1_json, f2_json) == verif
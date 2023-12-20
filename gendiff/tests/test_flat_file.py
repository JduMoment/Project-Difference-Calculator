from gendiff.generate_diff import generate_diff
from gendiff.file_to_dict import transform_to_dict


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()

def test_flat_file():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.json',
        'gendiff/tests/fixtures/file2_for_test.json'
        )
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.yml',
        'gendiff/tests/fixtures/file2_for_test.yml'
        )
    verif_file = read_file('gendiff/tests/fixtures/test_expected_flat.txt')
    assert generate_diff(f1_json, f2_json) == verif_file
    assert generate_diff(f1_yml, f2_yml) == verif_file

def test_empty_file():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file2_for_test.json',
        'gendiff/tests/fixtures//file3_for_test.json'
        )
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file2_for_test.yml',
        'gendiff/tests/fixtures/file3_for_test.yml'
        )
    verif_file = read_file('gendiff/tests/fixtures/test_expected_empty_file.txt')
    assert generate_diff(f2_json, f1_json) == verif_file
    assert generate_diff(f2_yml, f1_yml) == verif_file


def test_empty_files():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.json',
        'gendiff/tests/fixtures//file2_for_test.json'
        )
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file1_for_test.yml',
        'gendiff/tests/fixtures/file2_for_test.yml'
        )
    verif_file = read_file('gendiff/tests/fixtures/text_expected_empty_files.txt')
    assert generate_diff(f1_json, f2_json) == verif_file
    assert generate_diff(f1_yml, f2_yml) == verif_file


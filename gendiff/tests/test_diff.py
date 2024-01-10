from gendiff.generate_stylish_lines import generate_stylish_lines
from gendiff.file_to_dict import transform_to_dict


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
    verif_f = read_file('gendiff/tests/fixtures/test_expected_flat.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif_f
    assert generate_stylish_lines(f1_yml, f2_yml) == verif_f

def test_empty_files():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file3_for_test.json',
        'gendiff/tests/fixtures/file3_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file3_for_test.yml',
        'gendiff/tests/fixtures/file3_for_test.yml')
    verif_f = read_file('gendiff/tests/fixtures/text_expected_empty_files.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif_f
    assert generate_stylish_lines(f1_yml, f2_yml) == verif_f

def test_nested_stylish():
    f1_json, f2_json = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.json',
        'gendiff/tests/fixtures/file5_for_test.json')
    f1_yml, f2_yml = transform_to_dict(
        'gendiff/tests/fixtures/file4_for_test.yml',
        'gendiff/tests/fixtures/file5_for_test.yml')
    verif_f = read_file('gendiff/tests/fixtures/test_expected_stylish.txt')
    assert generate_stylish_lines(f1_json, f2_json) == verif_f
    assert generate_stylish_lines(f2_yml, f2_yml) == verif_f

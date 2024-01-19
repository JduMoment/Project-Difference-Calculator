from gendiff.construct_diff import construct_diff
from gendiff.file_to_dict import transform_to_dict
from gendiff.generate_stylish_lines import generate_stylish_lines
from gendiff.generate_plain_lines import generate_plain_lines
from gendiff.generate_json_file import python_to_json


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()


def test_generate_stylish_lines():
    flat_file_1, flat_file_2 = transform_to_dict('gendiff/tests/fixtures/file1_for_test.json',
                                                 'gendiff/tests/fixtures/file2_for_test.json')
    nested_file_1, nested_file_2 = transform_to_dict('gendiff/tests/fixtures/file4_for_test.json',
                                                     'gendiff/tests/fixtures/file5_for_test.json')
    diff_flat = construct_diff(nested_file_1, nested_file_2)
    diff_nested = construct_diff(nested_file_1, nested_file_2)
    verif_flat = read_file('gendiff/tests/fixtures/expect_flat_stylish.txt')
    verif_nested = read_file('gendiff/tests/fixtures/expect_nested_stylish.txt')
    assert generate_stylish_lines(diff_flat) == verif_flat
    assert generate_stylish_lines(diff_nested) == verif_nested


# def test_generate_plain_lines():
#     verif_flat = read_file('gendiff/tests/fixtures/expect_flat_plain.txt')
#     verif_nested = read_file('gendiff/tests/fixtures/expect_nested_plain.txt')
#     assert generate_plain_lines(diff_expected_flat) == verif_flat
#     assert generate_plain_lines(diff_expected_nested) == verif_nested
#
#
# def test_generate_json():
#     verif_json = read_file('gendiff/tests/fixtures/except_to_json.txt')
#     assert python_to_json(diff_expected_nested) == verif_json
#
#
# def test_empty_files():
#     verif_empty = read_file('gendiff/tests/fixtures/expect_empty_files.txt')
#     empty_file = None
#     assert generate_stylish_lines(empty_file) == verif_empty
#     assert generate_plain_lines(empty_file) == verif_empty



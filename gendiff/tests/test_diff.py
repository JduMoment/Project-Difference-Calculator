from gendiff.generate_diff import generate_diff


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()


def test_generate_stylish_lines():
    result_flat = generate_diff('gendiff/tests/fixtures/file1_for_test.yml',
                                'gendiff/tests/fixtures/file2_for_test.json')
    result_nested = generate_diff('gendiff/tests/fixtures/file3_for_test.yml',
                                  'gendiff/tests/fixtures/file4_for_test.json')
    verif_flat = read_file('gendiff/tests/fixtures/expect_flat_stylish.txt')
    verif_nested = read_file('gendiff/tests/fixtures/expect_nested_stylish.txt')
    assert result_flat == verif_flat
    assert result_nested == verif_nested


def test_generate_plain_lines():
    result_flat = generate_diff('gendiff/tests/fixtures/file1_for_test.yml',
                                'gendiff/tests/fixtures/file2_for_test.json',
                                'plain')
    result_nested = generate_diff('gendiff/tests/fixtures/file3_for_test.yml',
                                  'gendiff/tests/fixtures/file4_for_test.json',
                                  'plain')
    verif_flat = read_file('gendiff/tests/fixtures/expect_flat_plain.txt')
    verif_nested = read_file('gendiff/tests/fixtures/expect_nested_plain.txt')
    assert result_flat == verif_flat
    assert result_nested == verif_nested

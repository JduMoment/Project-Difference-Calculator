from gendiff.generate_diff import generate_diff


def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()


def test_generate_stylish_lines():
    result = generate_diff('/home/kuraginivan/python-project-50/tests/fixtures/file3_for_test.json',
                           '/home/kuraginivan/python-project-50/tests/fixtures/file4_for_test.yml')
    verif = read_file('/home/kuraginivan/python-project-50/tests/fixtures/expect_stylish.txt')
    assert result == verif


def test_generate_plain_lines():
    result = generate_diff('/home/kuraginivan/python-project-50/tests/fixtures/file3_for_test.json',
                           '/home/kuraginivan/python-project-50/tests/fixtures/file4_for_test.yml',
                           'plain')
    verif = read_file('/home/kuraginivan/python-project-50/tests/fixtures/expect_plain.txt')
    assert result == verif

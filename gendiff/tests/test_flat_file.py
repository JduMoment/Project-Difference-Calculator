from gendiff.flat_file import generate_diff


def test_flat_file():
    with open('gendiff/tests/fixtures/test_expected_flat.txt', 'r') as right:
        file1 = 'gendiff/tests/fixtures/file1_for_test.json'
        file2 = 'gendiff/tests/fixtures//file2_for_test.json'
        assert generate_diff(file1, file2) == right.read()


def test_empty_file():
    with open('gendiff/tests/fixtures/test_expected_empty_file.txt', 'r') as right:
        file1 = 'gendiff/tests/fixtures/file2_for_test.json'
        file2 = 'gendiff/tests/fixtures/file3_for_test.json'
        assert generate_diff(file2, file1) == right.read()


def test_empty_files():
    with open('gendiff/tests/fixtures/text_expected_empty_files.txt', 'r') as right:
        file1 = 'gendiff/tests/fixtures/file3_for_test.json'
        file2 = 'gendiff/tests/fixtures/file3_for_test.json'
        assert generate_diff(file1, file2) == right.read()


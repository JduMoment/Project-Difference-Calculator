from gendiff.flat_file import generate_diff
from gendiff.parse_args import parse_args

def test_flat_file():
    right = ''.join(['{\n', '  -follow: false\n', '   host: hexlet.io\n',
                    '  -proxy: 123.234.53.22\n', '  -timeout: 50\n',
                    '  +timeout: 20\n', '  +verbose: true\n', '}'])
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures//file2.json'
    assert generate_diff(file1, file2) == right

def test_empty_file():
    right = ''.join(['{\n', '  +host: hexlet.io\n', '  +timeout: 20\n',
                    '  +verbose: true\n', '}'])
    file1 = 'gendiff/tests/fixtures/file2.json'
    file2 = 'gendiff/tests/fixtures/file3.json'
    assert generate_diff(file2, file1) == right

def test_empty_files():
    right = None
    file1 = 'gendiff/tests/fixtures/file3.json'
    file2 = 'gendiff/tests/fixtures/file3.json'
    assert generate_diff(file1, file2) == right

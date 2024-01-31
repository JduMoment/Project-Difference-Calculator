from gendiff.generate_diff import generate_diff
import os

def read_file(path_to_expected_file):
    file = open(path_to_expected_file, 'r')
    return file.read()


def test_generate_stylish_lines():
    result_stylish = generate_diff((os.path.join(os.path.dirname(__file__), 'fixtures', 'file3_for_test.json')),
                                   (os.path.join(os.path.dirname(__file__), 'fixtures', 'file4_for_test.json')))
    verif_stylish = read_file((os.path.join(os.path.dirname(__file__), 'fixtures', 'expect_stylish.txt')))
    result_plain = generate_diff((os.path.join(os.path.dirname(__file__), 'fixtures', 'file3_for_test.yml')),
                                 (os.path.join(os.path.dirname(__file__), 'fixtures', 'file4_for_test.yml')),
                    'plain')
    verif_plain = read_file((os.path.join(os.path.dirname(__file__), 'fixtures', 'expect_plain.txt')))
    assert result_stylish == verif_stylish
    assert result_plain == verif_plain

import pytest

from gendiff.generate_diff import generate_diff
import os


def read_file(path_to_expected_file):
    with open(path_to_expected_file) as file:
        return file.read()


@pytest.mark.parametrize(
    'first_file, second_file, formatter, res',
    [
        (
            os.path.join(os.path.dirname(__file__), 'fixtures', 'file3_for_test.json'),
            os.path.join(os.path.dirname(__file__), 'fixtures', 'file4_for_test.json'),
            'stylish',
            read_file(os.path.join(os.path.dirname(__file__), 'fixtures', 'expect_stylish.txt'))
        ),
        (
            os.path.join(os.path.dirname(__file__), 'fixtures', 'file3_for_test.yml'),
            os.path.join(os.path.dirname(__file__), 'fixtures', 'file4_for_test.yml'),
            'plain',
            read_file(os.path.join(os.path.dirname(__file__), 'fixtures', 'expect_plain.txt'))
        )
    ]
)
def test_formatters(first_file, second_file, formatter, res):
    assert generate_diff(first_file, second_file, formatter) == res
    assert generate_diff(first_file, second_file, formatter) == res


def test_unknown_format():
    with pytest.raises(TypeError) as exc_info:
        generate_diff((os.path.join(os.path.dirname(__file__), 'fixtures', 'unknown_file.txt')),
                      (os.path.join(os.path.dirname(__file__), 'fixtures', 'unknown_file.txt')))
    assert exc_info.value.args[0] == 'The file format is not supported.'

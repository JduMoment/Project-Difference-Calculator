from gendiff.errors import FormatterError
from gendiff.formatters.stylish import generate_stylish_lines
from gendiff.formatters.plain import generate_plain_lines
from gendiff.formatters.to_json import python_to_json


def define_formatter(diff_tree, format_name):
    if format_name == 'stylish':
        return generate_stylish_lines(diff_tree)
    elif format_name == 'plain':
        return generate_plain_lines(diff_tree)
    elif format_name == 'json':
        return python_to_json(diff_tree)
    else:
        raise FormatterError(f"Format {format_name} is not supported.")

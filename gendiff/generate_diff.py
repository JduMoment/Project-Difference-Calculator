from gendiff.file_to_dict import transform_to_dict
from gendiff.construct_diff import build_diff
from gendiff.generate_stylish_lines import generate_stylish_lines
from gendiff.generate_plain_lines import generate_plain_lines
from gendiff.generate_json_file import python_to_json


def generate_diff(file_path_1, file_path_2, format_name):
    file1, file2 = transform_to_dict(file_path_1, file_path_2)
    diff = build_diff(file1, file2)
    if format_name == 'stylish':
        return generate_stylish_lines(diff)
    elif format_name == 'plain':
        return generate_plain_lines(diff)
    elif format_name == 'json':
        return python_to_json(diff)

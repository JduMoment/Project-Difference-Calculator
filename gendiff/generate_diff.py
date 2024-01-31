from gendiff.construct_diff import build_diff
from gendiff.formaters.stylish import generate_stylish_lines
from gendiff.formaters.plain import generate_plain_lines
from gendiff.formaters.json import python_to_json
from gendiff.file_to_dict import get_data


def generate_diff(file_path_1, file_path_2, format_name='stylish'):
    file1, file2 = get_data(file_path_1), get_data(file_path_2)
    diff = build_diff(file1, file2)
    if format_name == 'stylish':
        return generate_stylish_lines(diff)
    elif format_name == 'plain':
        return generate_plain_lines(diff)
    elif format_name == 'json':
        return python_to_json(diff)

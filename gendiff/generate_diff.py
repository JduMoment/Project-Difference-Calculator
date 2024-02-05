from gendiff.construct_diff import build_diff
from gendiff.file_to_dict import get_data
from gendiff.formatters.define_formatter import define_formatter


def generate_diff(file_path_1, file_path_2, format_name='stylish'):
    file1 = get_data(file_path_1)
    file2 = get_data(file_path_2)
    diff = build_diff(file1, file2)
    return define_formatter(diff, format_name)


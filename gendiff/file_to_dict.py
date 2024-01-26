import yaml
import json
import os


def open_file(file):
    open_file = open(file)
    return open_file


def transform_to_dict(path_to_file1, path_to_file2):
    _, format_file1 = os.path.splitext(path_to_file1)
    _, format_file_2 = os.path.splitext(path_to_file2)
    if format_file1 == '.json':
        file1 = json.load(open_file(path_to_file1))
    if format_file_2 == '.json':
        file2 = json.load(open_file(path_to_file2))
    if format_file1 == '.yaml' or format_file1 == '.yml':
        file1 = yaml.load(open_file(path_to_file1), Loader=yaml.FullLoader)
    if format_file_2 == '.yaml' or format_file_2 == '.yml':
        file2 = yaml.load(open_file(path_to_file2), Loader=yaml.FullLoader)
    return file1, file2

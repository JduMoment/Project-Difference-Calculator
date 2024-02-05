import yaml
import json
import os


def transform_to_dict(data, format_data):
    if format_data.lower() == 'json':
        return json.load(data)
    elif format_data.lower() in ['yaml', 'yml']:
        return yaml.load(data, Loader=yaml.FullLoader)
    raise TypeError('The file format is not supported.')


def get_data(path_to_file):
    _, format_file = os.path.splitext(path_to_file)
    with open(path_to_file, 'r') as file:
        return transform_to_dict(file, format_file[1:])

import yaml
import json
import os

def open_json(file):
    try:
        open_file = json.load(open(file))
    except json.decoder.JSONDecodeError:
        open_file = None
    return open_file

def transform_to_dict(path_to_file1, path_to_file2):
    # ff — абривиатура от format_file
    _, ff1 = os.path.splitext(path_to_file1)
    _, ff2 = os.path.splitext(path_to_file2)
    if ff1 == '.json':
         file1 = open_json(path_to_file1)
    if ff2 == '.json':
        file2 = open_json(path_to_file2)
    if ff1 == '.yaml' or ff1 == '.yml':
        file1 = yaml.load(open(path_to_file1), Loader=yaml.FullLoader)
    if ff2 == '.yaml' or ff2 == '.yml':
        file2 = yaml.load(open(path_to_file2), Loader=yaml.FullLoader)
    return file1, file2

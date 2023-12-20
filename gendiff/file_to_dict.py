import yaml
import json
import os


def transform_to_dict(path_to_file1, path_to_file2):
    # ff — абривиатура от format_file
    _, ff1 = os.path.splitext(path_to_file1)
    _, ff2 = os.path.splitext(path_to_file2)
    if ff1 == '.json' and ff2 == '.json':
        try:
            file1 = json.load(open(path_to_file1))
            file2 = json.load(open(path_to_file2))
        except json.decoder.JSONDecodeError:
            file1 = None
            file2 = None
        return file1, file2
    if ff1 == '.yaml' or ff1 == '.yml' and ff2 == '.yaml' or ff2 == '.yml':
        file1 = yaml.load(open(path_to_file1), Loader=yaml.FullLoader)
        file2 = yaml.load(open(path_to_file2), Loader=yaml.FullLoader)
        return file1, file2

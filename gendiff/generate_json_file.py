import json


def python_to_json(diff_list):
    return json.dumps(diff_list, indent=2)

import json


def generate_diff(path_first, path_second):
    first_file = json.load(open(path_first))
    second_file = json.load(open(path_second))
    if len(first_file) == 0 and len(second_file) == 0:
        return ''
    keys_1 = list(first_file.keys())
    keys_list = list(first_file.keys()) + [key for key in second_file.keys()
                                           if key not in keys_1]
    result = ''
    for key in sorted(keys_list):
        if first_file.get(key) == second_file.get(key):
            result += f"   {key}: {first_file.get(key)}\n"
        elif key in first_file and key not in second_file:
            result += f"  -{key}: {first_file.get(key)}\n"
        elif key in second_file and key not in first_file:
            result += f"  +{key}: {second_file.get(key)}\n"
        else:
            result += f"  -{key}: {first_file.get(key)}\n"
            result += f"  +{key}: {second_file.get(key)}\n"
    result = '{\n' + result.lower() + '}'
    return result

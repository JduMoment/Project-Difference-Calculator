def generate_diff(first_file, second_file):
    if first_file is None and second_file is None:
        return ''
    keys_list = set(list(first_file.keys()) + list(second_file.keys()))
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

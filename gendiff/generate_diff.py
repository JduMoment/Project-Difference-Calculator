def generate_diff(first_file, second_file):
    if first_file == None and second_file == None:
        return
    keys = list(first_file.keys())
    keys_list = list(first_file.keys()) + [key for key in second_file.keys()
                                        if key not in keys]
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

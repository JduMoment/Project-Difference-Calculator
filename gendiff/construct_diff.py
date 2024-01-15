# from file_to_dict import transform_to_dict

IN_FIRST = 'IN_FIRST'
SAME = 'SAME'
IN_SECOND = 'IN_SECOND'
CHANGED = 'CHANGED'
EMPTY = 'EMPTY'

# file1, file2 = transform_to_dict('gendiff/tests/fixtures/file4_for_test.json', 'gendiff/tests/fixtures/file5_for_test.json')

def make_dict(key, value, changes, value_2 = EMPTY):
    if value_2 != EMPTY:
        return dict(
            key=key,
            old_value=value,
            new_value=value_2,
            changes=changes,
        )
    return dict(
        key=key,
        value=value,
        changes=changes,
    )

def construct_diff(dict_1: dict, dict_2: dict) -> list:
    diff_list = []
    all_keys = sorted(set(dict_1.keys()) | set(dict_2.keys()))
    for key in all_keys:
        value_dict_1 = dict_1.get(key, EMPTY)
        value_dict_2 = dict_2.get(key, EMPTY)
        if key not in dict_2:
            diff_list.append(make_dict(key, value_dict_1, IN_FIRST))
        elif key not in dict_1:
            diff_list.append(make_dict(key, value_dict_2, IN_SECOND))
        elif value_dict_1 == value_dict_2:
            diff_list.append(make_dict(key, value_dict_1, SAME))
        elif isinstance(value_dict_1, dict) and isinstance(value_dict_2, dict):
            construct = construct_diff(value_dict_1, value_dict_2)
            diff_list.append(make_dict(key, construct, CHANGED))
        else:
            diff_list.append(make_dict(key, value_dict_1, CHANGED, value_dict_2))
    return diff_list

# from pprint import pprint

# pprint(construct_diff(file1, file2), sort_dicts=False)
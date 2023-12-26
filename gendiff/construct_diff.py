from json import load

with open('gendiff/tests/fixtures/file1.json', 'r') as file:
    file1 = load(file)
with open('gendiff/tests/fixtures/file2.json', 'r') as file:
    file2 = load(file)

def make_dict(key, new_value, old_value, changes):
    return{
        'key': key,
        'old_value': old_value,
        'new_value': new_value,
        'diff': changes,
    }

IN_FIRST = 'IN_FIRST'
SAME = 'SAME'
IN_SECOND = 'IN_SECOND'
CHANGED = 'CHANGED'
EMPTY = 'EMPTY'


def construct_diff(dict_1: dict, dict_2: dict) -> list:
    diff_list = []
    all_keys = sorted(set(dict_1.keys()) | set(dict_2.keys()))
    for key in all_keys:
        value_dict_1 = dict_1.get(key, EMPTY)
        value_dict_2 = dict_2.get(key, EMPTY)
        if key not in dict_2:
            diff_list.append(make_dict(key, value_dict_1,
                                       value_dict_2, IN_FIRST))
        elif key not in dict_1:
            diff_list.append(make_dict(key, value_dict_1,
                                       value_dict_2, IN_SECOND))
        elif value_dict_1 == value_dict_2:
            diff_list.append(make_dict(key, value_dict_1,
                                       value_dict_2, SAME))
        elif isinstance(value_dict_1, dict) and isinstance(value_dict_2, dict):
            construct = construct_diff(value_dict_1, value_dict_2)
            diff_list.append(make_dict(key, value_dict_1, value_dict_1, construct))
        else:
            diff_list.append(make_dict(key, value_dict_1, value_dict_2, CHANGED))
    return diff_list

from pprint import pp

pp(construct_diff(file1, file2), sort_dicts=False)

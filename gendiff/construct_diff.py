from typing import Dict, List

IN_FIRST = 'IN_FIRST'
SAME = 'SAME'
IN_SECOND = 'IN_SECOND'
CHANGED = 'CHANGED'
NESTED = 'NESTED'
EMPTY = 'EMPTY'


def make_node(key, value, type, children=None, value_2=EMPTY) -> Dict:
    if value_2 != EMPTY:
        return dict(
            key=key,
            old_value=value,
            new_value=value_2,
            type=type,
        )
    return dict(
        key=key,
        value=value,
        children=children
        type=type,
    )


def construct_diff(data_1: Dict, data_2: Dict) -> List:
    diff = []
    all_keys = sorted(set(data_1.keys()) | set(data_2.keys()))
    for key in all_keys:
        value_data_1 = data_1.get(key, EMPTY)
        value_data_2 = data_2.get(key, EMPTY)
        if key not in data_2:
            diff.append(make_node(key, value_data_1, IN_FIRST))
        elif key not in data_1:
            diff.append(make_node(key, value_data_2, IN_SECOND))
        elif value_data_1 == value_data_2:
            diff.append(make_node(key, value_data_1, SAME))
        elif isinstance(value_data_1, dict) and isinstance(value_data_2, dict):
            construct = construct_diff(value_data_1, value_data_2)
            #construct добавляется в children
            diff.append(make_node(key, construct, NESTED))
        else:
            diff.append(make_node(key, value_data_1, CHANGED, value_data_2))
    return diff

def build_diff(data_1, data_2):
    return {
        'type': 'root',
        'children': construct_diff(data_1, data_2),
    }
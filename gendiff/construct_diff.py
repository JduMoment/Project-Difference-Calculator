from typing import Dict, List

DELETED = 'DELETED'
SAME = 'SAME'
ADDED = 'ADDED'
CHANGED = 'CHANGED'
NESTED = 'NESTED'


def construct_diff(data_1: Dict, data_2: Dict) -> List:
    diff = []
    all_keys = sorted(set(data_1.keys()) | set(data_2.keys()))
    for key in all_keys:
        value_data_1 = data_1.get(key, 'EMPTY')
        value_data_2 = data_2.get(key, 'EMPTY')
        if key not in data_2:
            diff.append(dict(
                key=key,
                value=value_data_1,
                node_type=DELETED,
            ))
        elif key not in data_1:
            diff.append(dict(
                key=key,
                new_value=value_data_2,
                change=ADDED,
            ))
        elif value_data_1 == value_data_2:
            diff.append(dict(
                key=key,
                old_value=value_data_1,
                change=SAME,
            ))
        elif isinstance(value_data_1, dict) and isinstance(value_data_2, dict):
            construct = build_diff(value_data_1, value_data_2)
            diff.append(dict(
                key=key,
                value=construct,
                change=NESTED,
            ))
        else:
            diff.append(dict(
                key=key,
                old_value=value_data_1,
                new_value=value_data_2,
                change=CHANGED,
            ))
    return diff


def build_diff(data_1, data_2):
    return dict(
        type='root',
        children=construct_diff(data_1, data_2),
    )
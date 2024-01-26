from typing import Dict, List
from enum import Enum


class NodeType(Enum):
    deleted = 'DELETED'
    same = 'SAME'
    added = 'ADDED'
    changed = 'CHANGED'
    nested = 'NESTED'


def construct_diff(data_1: Dict, data_2: Dict) -> List:
    diff = []
    all_keys = sorted(set(data_1.keys()) | set(data_2.keys()))
    for key in all_keys:
        value_data_1 = data_1.get(key)
        value_data_2 = data_2.get(key)
        if key not in data_2:
            diff.append(dict(
                key=key,
                value=value_data_1,
                node_type=NodeType.deleted.value,
            ))
        elif key not in data_1:
            diff.append(dict(
                key=key,
                value=value_data_2,
                node_type=NodeType.added.value,
            ))
        elif value_data_1 == value_data_2:
            diff.append(dict(
                key=key,
                value=value_data_1,
                node_type=NodeType.same.value,
            ))
        elif isinstance(value_data_1, dict) and isinstance(value_data_2, dict):
            children = construct_diff(value_data_1, value_data_2)
            diff.append(dict(
                key=key,
                children=children,
                node_type=NodeType.nested.value,
            ))
        else:
            diff.append(dict(
                key=key,
                old_value=value_data_1,
                new_value=value_data_2,
                node_type=NodeType.changed.value,
            ))
    return diff


def build_diff(data_1, data_2):
    return dict(
        node_type='root',
        children=construct_diff(data_1, data_2),
    )

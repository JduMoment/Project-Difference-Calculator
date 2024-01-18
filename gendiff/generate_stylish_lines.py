DEPTH_STEP = 1
GAP = 4
LEFT_SHIFT = 2

dfflst = {'type': 'root',
 'children': [{'key': 'common',
               'value': {'type': 'root',
                         'children': [{'key': 'follow',
                                       'value': False,
                                       'node_type': 'ADDED'},
                                      {'key': 'setting1',
                                       'value': 'Value 1',
                                       'node_type': 'SAME'},
                                      {'key': 'setting2',
                                       'value': 200,
                                       'node_type': 'DELETED'},
                                      {'key': 'setting3',
                                       'old_value': True,
                                       'new_value': None,
                                       'node_type': 'CHANGED'},
                                      {'key': 'setting4',
                                       'value': 'blah blah',
                                       'node_type': 'ADDED'},
                                      {'key': 'setting5',
                                       'value': {'key5': 'value5'},
                                       'node_type': 'ADDED'},
                                      {'key': 'setting6',
                                       'value': {'type': 'root',
                                                 'children': [{'key': 'doge',
                                                               'value': {'type': 'root',
                                                                         'children': [{'key': 'wow',
                                                                                       'old_value': '',
                                                                                       'new_value': 'so '
                                                                                                    'much',
                                                                                       'node_type': 'CHANGED'}]},
                                                               'node_type': 'NESTED'},
                                                              {'key': 'key',
                                                               'value': 'value',
                                                               'node_type': 'SAME'},
                                                              {'key': 'ops',
                                                               'value': 'vops',
                                                               'node_type': 'ADDED'}]},
                                       'node_type': 'NESTED'}]},
               'node_type': 'NESTED'},
              {'key': 'group1',
               'value': {'type': 'root',
                         'children': [{'key': 'baz',
                                       'old_value': 'bas',
                                       'new_value': 'bars',
                                       'node_type': 'CHANGED'},
                                      {'key': 'foo',
                                       'value': 'bar',
                                       'node_type': 'SAME'},
                                      {'key': 'nest',
                                       'old_value': {'key': 'value'},
                                       'new_value': 'str',
                                       'node_type': 'CHANGED'}]},
               'node_type': 'NESTED'},
              {'key': 'group2',
               'value': {'abc': 12345, 'deep': {'id': 45}},
               'node_type': 'DELETED'},
              {'key': 'group3',
               'value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
               'node_type': 'ADDED'}]}


def make_string(key, value, depth, diff=' '):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    lines = []
    shift = f"{' ' * (depth * GAP - LEFT_SHIFT)}"
    if isinstance(value, dict):
        lines.append(f"{shift}{diff} {key}: " + '{')
        for k, v in value.items():
            result = make_string(k, v, depth + DEPTH_STEP)
            lines.append(result)
        lines.append(f"{shift}  " + '}')
    else:
        lines.append(f"{shift}{diff} {key}: {value}")
    return '\n'.join(lines)


def generate_stylish_lines(diff_tree, depth=0):
    if diff_tree is None or len(diff_tree) == 0:
        return ''
    lines = []
    children = diff_tree['children']
    for child in children:
        key = child.get('key')
        value = child.get('value')
        node_type = child.get('node_type')
        if node_type == 'NESTED':
            lines.append(f"{' ' * ((depth + 1) * GAP - LEFT_SHIFT)}  {key}: " + '{')
            result = generate_stylish_lines(child.get('value'), depth + 1)
            lines.append(result)
        elif node_type == 'DELETED':
            lines.append(make_string(key, value, depth + 1, '-'))
        elif node_type == 'ADDED':
            lines.append(make_string(key, value, depth + 1, '+'))
        elif node_type == 'CHANGED':
            lines.append(make_string(key, child.get('old_value'), depth + 1, '-'))
            lines.append(make_string(key, child.get('new_value'), depth + 1, '+'))
        else:
            lines.append(make_string(key, value, depth + 1))
    lines.append(f"{' ' * (depth * GAP - LEFT_SHIFT)}  " + '}')
    return '\n'.join(lines)


print(generate_stylish_lines(dfflst))



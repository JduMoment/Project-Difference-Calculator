DEPTH_STEP = 1
GAP = 4
LEFT_SHIFT = 2

dfflst = {'type': 'root',
 'children': [{'key': 'common',
               'value': {'type': 'root',
                         'children': [{'key': 'follow',
                                       'old_value': 'EMPTY',
                                       'new_value': False,
                                       'type': 'leaf',
                                       'change': 'IN_SECOND'},
                                      {'key': 'setting1',
                                       'old_value': 'Value 1',
                                       'new_value': 'Value 1',
                                       'type': 'leaf',
                                       'change': 'SAME'},
                                      {'key': 'setting2',
                                       'old_value': 200,
                                       'new_value': 'EMPTY',
                                       'type': 'leaf',
                                       'change': 'IN_FIRST'},
                                      {'key': 'setting3',
                                       'old_value': True,
                                       'new_value': None,
                                       'type': 'leaf',
                                       'change': 'CHANGED'},
                                      {'key': 'setting4',
                                       'old_value': 'EMPTY',
                                       'new_value': 'blah blah',
                                       'type': 'leaf',
                                       'change': 'IN_SECOND'},
                                      {'key': 'setting5',
                                       'old_value': 'EMPTY',
                                       'new_value': {'key5': 'value5'},
                                       'type': 'leaf',
                                       'change': 'IN_SECOND'},
                                      {'key': 'setting6',
                                       'value': {'type': 'root',
                                                 'children': [{'key': 'doge',
                                                               'value': {'type': 'root',
                                                                         'children': [{'key': 'wow',
                                                                                       'old_value': '',
                                                                                       'new_value': 'so '
                                                                                                    'much',
                                                                                       'type': 'leaf',
                                                                                       'change': 'CHANGED'}]},
                                                               'type': 'leaf',
                                                               'change': 'NESTED'},
                                                              {'key': 'key',
                                                               'old_value': 'value',
                                                               'new_value': 'value',
                                                               'type': 'leaf',
                                                               'change': 'SAME'},
                                                              {'key': 'ops',
                                                               'old_value': 'EMPTY',
                                                               'new_value': 'vops',
                                                               'type': 'leaf',
                                                               'change': 'IN_SECOND'}]},
                                       'type': 'leaf',
                                       'change': 'NESTED'}]},
               'type': 'leaf',
               'change': 'NESTED'},
              {'key': 'group1',
               'value': {'type': 'root',
                         'children': [{'key': 'baz',
                                       'old_value': 'bas',
                                       'new_value': 'bars',
                                       'type': 'leaf',
                                       'change': 'CHANGED'},
                                      {'key': 'foo',
                                       'old_value': 'bar',
                                       'new_value': 'bar',
                                       'type': 'leaf',
                                       'change': 'SAME'},
                                      {'key': 'nest',
                                       'old_value': {'key': 'value'},
                                       'new_value': 'str',
                                       'type': 'leaf',
                                       'change': 'CHANGED'}]},
               'type': 'leaf',
               'change': 'NESTED'},
              {'key': 'group2',
               'old_value': {'abc': 12345, 'deep': {'id': 45}},
               'new_value': 'EMPTY',
               'type': 'leaf',
               'change': 'IN_FIRST'},
              {'key': 'group3',
               'old_value': 'EMPTY',
               'new_value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
               'type': 'leaf',
               'change': 'IN_SECOND'}]}

# def make_line(key, old_value, new_value, change, depth, diff):
#     if value is None:
#         value = 'null'
#     elif value is True or value is False:
#         value = str(value).lower()
#     if isinstance(value, dict) or isinstance(value, list):
#         return f"{' ' * (depth * GAP - LEFT_SHIFT)}{diff} {key}" + ': {'
#     else:
#         return f"{' ' * (depth * GAP - LEFT_SHIFT)}{diff} {key}: {value}"


def generate_stylish_lines(diff_tree, depth=0):
    if diff_tree is None or len(diff_tree) == 0:
        return ''
    lines = []
    shift = f"{' ' * (depth * GAP - LEFT_SHIFT)}"
    childrens = diff_tree['children']
    for child in childrens:
        key = child.get('key')
        old_value = child.get('old_value')
        new_value = child.get('new_value')
        change = child.get('change')
        if child.get('value', None) is not None:
            lines.append(f"{shift}  {key}: ")
            result = generate_stylish_lines(child.get('value'), depth + DEPTH_STEP)
            lines.append(result)
        if change == 'IN_SECOND':
            lines.append(f"{shift}- {key}: {new_value}")
        elif change == 'IN_FIRST':
            lines.append(f"{shift}+ {key}: {old_value}")
        elif change == 'CHANGED':
            lines.append(f"{shift}- {key}: {old_value}")
            lines.append(f"{shift}+ {key}: {new_value}")
        elif change == 'SAME':
            lines.append(f"{shift}  {key}: {new_value}")
    return '\n'.join(lines)


print(generate_stylish_lines(dfflst))


# def generate_stylish_lines(diff_list, depth=0):
#     if diff_list is None or len(diff_list) == 0:
#         return ''
#     lines = []
#     if depth == 0:
#         depth += 1
#         lines.append('{')
#     if isinstance(diff_list, list):
#         for every_dict in diff_list:
#             key = every_dict['key']
#             value = every_dict.get('value')
#             if every_dict['changes'] == 'IN_FIRST':
#                 lines.append(make_line(key, value, depth, '-'))
#                 if isinstance(value, dict):
#                     result = generate_stylish_lines(value, depth + DEPTH_STEP)
#                     lines.append(result)
#             elif every_dict['changes'] == 'IN_SECOND':
#                 lines.append(make_line(key, value, depth, '+'))
#                 if isinstance(value, dict):
#                     result = generate_stylish_lines(value, depth + DEPTH_STEP)
#                     lines.append(result)
#             elif every_dict['changes'] == 'SAME':
#                 lines.append(make_line(key, value, depth, ' '))
#                 if isinstance(value, dict):
#                     result = generate_stylish_lines(value, depth + DEPTH_STEP)
#                     lines.append(result)
#             elif every_dict['changes'] == 'CHANGED':
#                 if 'old_value' in every_dict:
#                     lines.append(make_line(key, every_dict['old_value'],
#                                            depth, '-'))
#                     if isinstance(every_dict['old_value'], dict):
#                         result = generate_stylish_lines(every_dict['old_value'],
#                                                         depth + DEPTH_STEP)
#                         lines.append(result)
#                     lines.append(make_line(key, every_dict['new_value'],
#                                            depth, '+'))
#                     if isinstance(every_dict['new_value'], dict):
#                         result = generate_stylish_lines(every_dict['new_value'],
#                                                         depth + DEPTH_STEP)
#                         lines.append(result)
#                 elif isinstance(value, list):
#                     lines.append(f" {make_line(key, value, depth, '')}")
#                     result = generate_stylish_lines(value, depth + DEPTH_STEP)
#                     lines.append(result)
#     elif isinstance(diff_list, dict):
#         for k, v in diff_list.items():
#             lines.append(f" {make_line(k, v, depth, '')}")
#             if isinstance(v, dict):
#                 result = generate_stylish_lines(v, depth + DEPTH_STEP)
#                 lines.append(result)
#     depth -= 1
#     lines.append(f"{' ' * (depth * GAP)}" + '}')
#     return '\n'.join(lines)

diff = [{'key': 'common',
        'value': [{'key': 'follow', 'value': False, 'changes': 'IN_SECOND'},
                    {'key': 'setting1', 'value': 'Value 1', 'changes': 'SAME'},
                    {'key': 'setting2', 'value': 200, 'changes': 'IN_FIRST'},
                    {'key': 'setting3', 'value': True, 'changes': 'CHANGED'},
                    {'key': 'setting4', 'value': 'blah blah', 'changes': 'IN_SECOND'},
                    {'key': 'setting5',
                    'value': {'key5': 'value5'},
                    'changes': 'IN_SECOND'},
                    {'key': 'setting6',
                    'value': [{'key': 'doge',
                                'value': [{'key': 'wow',
                                        'old_value': '',
                                        'new_value': 'so much',
                                        'changes': 'CHANGED'}],
                                'changes': 'CHANGED'},
                            {'key': 'key', 'value': 'value', 'changes': 'SAME'},
                            {'key': 'ops', 'value': 'vops', 'changes': 'IN_SECOND'}],
                    'changes': 'CHANGED'}],
        'changes': 'CHANGED'},
        {'key': 'group1',
        'value': [{'key': 'baz',
                    'old_value': 'bas',
                    'new_value': 'bars',
                    'changes': 'CHANGED'},
                    {'key': 'foo', 'value': 'bar', 'changes': 'SAME'},
                    {'key': 'nest',
                    'old_value': {'key': 'value'},
                    'new_value': 'str',
                    'changes': 'CHANGED'}],
        'changes': 'CHANGED'},
        {'key': 'group2',
        'value': {'abc': 12345, 'deep': {'id': 45}},
        'changes': 'IN_FIRST'},
        {'key': 'group3',
        'value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
        'changes': 'IN_SECOND'}]

from pprint import pprint


def generate_diff(diff_list, depth = 1, line = ['{']):
    if isinstance(diff_list, list):
        for every_dict in diff_list:
            if every_dict['changes'] == 'IN_FIRST':
                if isinstance(every_dict['value'], dict):
                    line.append(f"{' ' * (depth * 4 - 2)}- {every_dict['key']}: " + '{')
                    generate_diff(every_dict['value'], depth + 1)
                else:
                    line.append(f"{' ' * (depth * 4 - 2)}- {every_dict['key']}: {every_dict['value']}")
            elif every_dict['changes'] == 'IN_SECOND':
                if isinstance(every_dict['value'], dict):
                    line.append(f"{' ' * (depth * 4 - 2)}+ {every_dict['key']}: " + '{')
                    generate_diff(every_dict['value'], depth + 1)
                else:
                    line.append(f"{' ' * (depth * 4 - 2)}+ {every_dict['key']}: {every_dict['value']}")
            elif every_dict['changes'] == 'SAME':
                if isinstance(every_dict['value'], dict):
                    line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}: {every_dict['value']}")
                else:
                    line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}: {every_dict['value']}")
            elif every_dict['changes'] == 'CHANGED':
                if 'old_value' in every_dict:
                    if isinstance(every_dict['old_value'], dict):
                        line.append(f"{' ' * (depth * 4 - 2)}- {every_dict['key']}: " + '{')
                        generate_diff(every_dict['old_value'], depth + 1)
                    else:
                        line.append(f"{' ' * (depth * 4 - 2)}- {every_dict['key']}: {every_dict['old_value']}")
                    if isinstance(every_dict['new_value'], dict):
                        line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}: " + '{')
                        generate_diff(every_dict['new_value'], depth + 1)
                    else:
                        line.append(f"{' ' * (depth * 4 - 2)}+ {every_dict['key']}: {every_dict['new_value']}")
                elif isinstance(every_dict['value'], list):
                    line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}" + ' {')
                    generate_diff(every_dict['value'], depth + 1)
    elif isinstance(diff_list, dict):
        for k, v in diff_list.items():
            if isinstance(v, dict):
                line.append(f"{' ' * (depth * 4 - 2)} {k}: " + '{')
                generate_diff(v, depth + 1)
            else:
                line.append(f"{' ' * (depth * 4 - 2)} {k}: {v}")
    line.append(f"{' ' * (depth * 4 - 4)}" + '}')
    line = '\n'.join(line)
    return line

print(generate_diff(diff))
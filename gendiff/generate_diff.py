diff = [{'key': 'common',
  'old_value': {'setting1': 'Value 1',
                'setting2': 200,
                'setting3': True,
                'setting6': {'key': 'value', 'doge': {'wow': ''}}},
  'new_value': {'setting1': 'Value 1',
                'setting2': 200,
                'setting3': True,
                'setting6': {'key': 'value', 'doge': {'wow': ''}}},
  'diff': [{'key': 'follow',
            'old_value': False,
            'new_value': 'EMPTY',
            'diff': 'IN_SECOND'},
           {'key': 'setting1',
            'old_value': 'Value 1',
            'new_value': 'Value 1',
            'diff': 'SAME'},
           {'key': 'setting2',
            'old_value': 'EMPTY',
            'new_value': 200,
            'diff': 'IN_FIRST'},
           {'key': 'setting3',
            'old_value': None,
            'new_value': True,
            'diff': 'CHANGED'},
           {'key': 'setting4',
            'old_value': 'blah blah',
            'new_value': 'EMPTY',
            'diff': 'IN_SECOND'},
           {'key': 'setting5',
            'old_value': {'key5': 'value5'},
            'new_value': 'EMPTY',
            'diff': 'IN_SECOND'},
           {'key': 'setting6',
            'old_value': {'key': 'value', 'doge': {'wow': ''}},
            'new_value': {'key': 'value', 'doge': {'wow': ''}},
            'diff': [{'key': 'doge',
                      'old_value': {'wow': ''},
                      'new_value': {'wow': ''},
                      'diff': [{'key': 'wow',
                                'old_value': 'so much',
                                'new_value': '',
                                'diff': 'CHANGED'}]},
                     {'key': 'key',
                      'old_value': 'value',
                      'new_value': 'value',
                      'diff': 'SAME'},
                     {'key': 'ops',
                      'old_value': 'vops',
                      'new_value': 'EMPTY',
                      'diff': 'IN_SECOND'}]}]},
 {'key': 'group1',
  'old_value': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
  'new_value': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
  'diff': [{'key': 'baz',
            'old_value': 'bars',
            'new_value': 'bas',
            'diff': 'CHANGED'},
           {'key': 'foo',
            'old_value': 'bar',
            'new_value': 'bar',
            'diff': 'SAME'},
           {'key': 'nest',
            'old_value': 'str',
            'new_value': {'key': 'value'},
            'diff': 'CHANGED'}]},
 {'key': 'group2',
  'old_value': 'EMPTY',
  'new_value': {'abc': 12345, 'deep': {'id': 45}},
  'diff': 'IN_FIRST'},
 {'key': 'group3',
  'old_value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
  'new_value': 'EMPTY',
  'diff': 'IN_SECOND'}]

from pprint import pprint


def generate_diff(diff_list, depth = 1):
    start_line = '{ \n'
    line = []
    for every_dict in diff_list:
        pprint(f"Сейчас берём ключ {every_dict}", sort_dicts=False)
        print(f"Вот такой у него ключ {}")
        if every_dict['diff'] == 'IN_FIRST':
            line.append(f"{' ' * (depth * 4 - 2)}- {every_dict['key']}" + ' {')
        elif every_dict['diff'] == 'IN_SECOND':
            line.append(f"{' ' * (depth * 4 - 2)}+ {every_dict['key']}" + ' {')
        elif every_dict['diff'] == 'SAME':
            line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}" + ' {')
        elif isinstance(every_dict['diff'], dict):
            print('Сработало!')
            line.append(f"{' ' * (depth * 4 - 2)}  {every_dict['key']}" + ' {')
            generate_diff(every_dict['diff'], depth + 1)
    print(line)

generate_diff(diff)
def processing_value(value):
    if value is None:
        return 'null'
    elif value is True or value is False:
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def generate_plain_lines(diff_list, parent=''):
    if diff_list is None or len(diff_list) == 0:
        return ''
    lines = []
    for every_dict in diff_list:
        key = every_dict['key']
        value = every_dict.get('value')
        changes = every_dict['changes']
        if changes == 'CHANGED':
            if isinstance(value, list):
                result = generate_plain_lines(value, parent + f"{key}.")
                lines.append(result)
            else:
                old_value = processing_value(every_dict['old_value'])
                new_value = processing_value(every_dict['new_value'])
                lines.append(f"Property '{parent}{key}' was updated. "
                             f"From {old_value} to {new_value}")
        elif changes == 'IN_SECOND':
            value = processing_value(value)
            if isinstance(value, dict):
                lines.append(f"Property '{parent}{key}' was added with value: "
                             f"[complex value]")
            else:
                lines.append(f"Property '{parent}{key}' was added with value: "
                             f"{value}")
        elif changes == 'IN_FIRST':
            value = processing_value(value)
            lines.append(f"Property '{parent}{key}' was removed")
    return '\n'.join(lines)

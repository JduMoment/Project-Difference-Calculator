def processing_value(value):
    if value == 'true' or value == 'false' or value == 'null':
        return value
    elif value is None:
        return ''
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"

def generate_plain_lines(diff_list, parent = ''):
    lines = []
    for every_dict in diff_list:
        key = every_dict['key']
        value = every_dict.get('value')
        changes = every_dict['changes']
        if changes == 'CHANGED':
            if isinstance(value, list):
                result = generate_plain_lines(value, parent + f"{key}.")
            else:
                old_value = processing_value(every_dict['old_value'])
                new_value = processing_value(every_dict['new_value'])
                lines.append(f"Property '{parent}{key}' was updated. "
                            f"From {old_value} to {new_value}")
        elif changes == 'IN_SECOND':
            value = processing_value(value)
            if isinstance(value, dict):
                lines.append(f"Property '{parent}{key}' was added with value: [complex value]")
            else:
                lines.append(f"Property '{parent}{key}' was added with value: {value}")
        elif changes == 'IN_FIRST':
            value = processing_value(value)
            lines.append(f"Property '{parent}{key}' was removed")
    return lines
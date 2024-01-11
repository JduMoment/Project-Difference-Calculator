def make_line(key, value, depth, diff):
    if isinstance(value, dict) or isinstance(value, list):
        return f"{' ' * (depth * 4 - 2)}{diff} {key}: " + '{'
    else:
        return (f"{' ' * (depth * 4 - 2)}{diff} {key}: {value}")


def generate_stylish_lines(diff_list, depth = 1):
    lines = []
    if depth == 1:
        lines.append('{')
    if isinstance(diff_list, list):
        for every_dict in diff_list:
            key = every_dict['key']
            value = every_dict.get('value')
            if every_dict['changes'] == 'IN_FIRST':
                lines.append(make_line(key, value, depth, '-'))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + 1)
                    lines.append(result)
            elif every_dict['changes'] == 'IN_SECOND':
                lines.append(make_line(key, value, depth, '+'))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + 1)
                    lines.append(result)
            elif every_dict['changes'] == 'SAME':
                lines.append(make_line(key, value, depth, ' '))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + 1)
                    lines.append(result)
            elif every_dict['changes'] == 'CHANGED':
                if 'old_value' in every_dict:
                    lines.append(make_line(key, every_dict['old_value'], depth, '-'))
                    if isinstance(every_dict['old_value'], dict):
                        result = generate_stylish_lines(every_dict['old_value'], depth + 1)
                        lines.append(result)
                    lines.append(make_line(key, every_dict['new_value'], depth, '+'))
                    if isinstance(every_dict['new_value'], dict):
                        result = generate_stylish_lines(every_dict['new_value'], depth + 1)
                        lines.append(result)
                elif isinstance(value, list):
                    lines.append(f" {make_line(key, value, depth, '')}")
                    result = generate_stylish_lines(value, depth + 1)
                    lines.append(result)
    elif isinstance(diff_list, dict):
        for k, v in diff_list.items():
            lines.append(f" {make_line(k, v, depth, '')}")
            if isinstance(v, dict):
                generate_stylish_lines(v, depth + 1)
    lines.append(f"{' ' * (depth * 4 - 4)}" + '}')
    return '\n'.join(lines)

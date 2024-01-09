def make_line(key, value, depth, diff):
    if isinstance(value, dict) or isinstance(value, list):
        return f"{' ' * (depth * 4 - 2)}{diff} {key}: " + '{'
    else:
        return (f"{' ' * (depth * 4 - 2)}{diff} {key}: {value}")

def generate_stylish_lines(diff_list, depth = 1, lines = ['{']):
    if isinstance(diff_list, list):
        for every_dict in diff_list:
            key = every_dict['key']
            if every_dict['changes'] == 'IN_FIRST':
                lines.append(make_line(key, every_dict['value'], depth, '-'))
                if isinstance(every_dict['value'], dict):
                    generate_stylish_lines(every_dict['value'], depth + 1)
            elif every_dict['changes'] == 'IN_SECOND':
                lines.append(make_line(key, every_dict['value'], depth, '+'))
                if isinstance(every_dict['value'], dict):
                    generate_stylish_lines(every_dict['value'], depth + 1)
            elif every_dict['changes'] == 'SAME':
                lines.append(make_line(key, every_dict['value'], depth, ' '))
                if isinstance(every_dict['value'], dict):
                    generate_stylish_lines(every_dict['value'], depth + 1)
            elif every_dict['changes'] == 'CHANGED':
                if 'old_value' in every_dict:
                    lines.append(make_line(key, every_dict['old_value'], depth, '-'))
                    if isinstance(every_dict['old_value'], dict):
                        generate_stylish_lines(every_dict['old_value'], depth + 1)
                    lines.append(make_line(key, every_dict['new_value'], depth, '+'))
                    if isinstance(every_dict['new_value'], dict):
                        generate_stylish_lines(every_dict['new_value'], depth + 1)
                elif isinstance(every_dict['value'], list):
                    make_line(key, every_dict['value'], depth, ' ')
                    generate_stylish_lines(every_dict['value'], depth + 1)
    elif isinstance(diff_list, dict):
        for k, v in diff_list.items():
            lines.append(f" {make_line(k, v, depth, '')}")
            if isinstance(v, dict):
                generate_stylish_lines(v, depth + 1)
    lines.append(f"{' ' * (depth * 4 - 4)}" + '}')
    return '\n'.join(lines)

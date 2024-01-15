DEPTH_STEP = 1
NUM_OF_INDENTS = 4
LEFT_SHIFT = 2

def make_line(key, value, depth, diff):
    if value is None:
        value = 'null'
    elif value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    if isinstance(value, dict) or isinstance(value, list):
        return f"{' ' * (depth * NUM_OF_INDENTS - LEFT_SHIFT)}{diff} {key}: " + '{'
    else:
        return (f"{' ' * (depth * NUM_OF_INDENTS - LEFT_SHIFT)}{diff} {key}: {value}")


def generate_stylish_lines(diff_list, depth = DEPTH_STEP):
    if diff_list is None:
        return None
    lines = []
    if depth == DEPTH_STEP:
        lines.append('{')
    if isinstance(diff_list, list):
        for every_dict in diff_list:
            key = every_dict['key']
            value = every_dict.get('value')
            if every_dict['changes'] == 'IN_FIRST':
                lines.append(make_line(key, value, depth, '-'))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + DEPTH_STEP)
                    lines.append(result)
            elif every_dict['changes'] == 'IN_SECOND':
                lines.append(make_line(key, value, depth, '+'))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + DEPTH_STEP)
                    lines.append(result)
            elif every_dict['changes'] == 'SAME':
                lines.append(make_line(key, value, depth, ' '))
                if isinstance(value, dict):
                    result = generate_stylish_lines(value, depth + DEPTH_STEP)
                    lines.append(result)
            elif every_dict['changes'] == 'CHANGED':
                if 'old_value' in every_dict:
                    lines.append(make_line(key, every_dict['old_value'], depth, '-'))
                    if isinstance(every_dict['old_value'], dict):
                        result = generate_stylish_lines(every_dict['old_value'], depth + DEPTH_STEP)
                        lines.append(result)
                    lines.append(make_line(key, every_dict['new_value'], depth, '+'))
                    if isinstance(every_dict['new_value'], dict):
                        result = generate_stylish_lines(every_dict['new_value'], depth + DEPTH_STEP)
                        lines.append(result)
                elif isinstance(value, list):
                    lines.append(f" {make_line(key, value, depth, '')}")
                    result = generate_stylish_lines(value, depth + DEPTH_STEP)
                    lines.append(result)
    elif isinstance(diff_list, dict):
        for k, v in diff_list.items():
            lines.append(f" {make_line(k, v, depth, '')}")
            if isinstance(v, dict):
                result = generate_stylish_lines(v, depth + DEPTH_STEP)
                lines.append(result)
    lines.append(f"{' ' * depth}" + '}')
    return '\n'.join(lines)
DEPTH_STEP = 1
GAP = 4
LEFT_SHIFT = 2


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
    key = diff_tree.get('key')
    value = diff_tree.get('value')
    node_type = diff_tree.get('node_type')
    if node_type == 'root':
        children = diff_tree['children']
        lines = []
        lines.append('{')
        for child in children:
            result = generate_stylish_lines(child, depth + DEPTH_STEP)
            lines.append(result)
        lines.append('}')
        return '\n'.join(lines)
    elif node_type == 'NESTED':
        children = diff_tree['children']
        lines = []
        for child in children:
            result = generate_stylish_lines(child, depth + 1)
            lines.append(result)
        result = '\n'.join(lines)
        return f"{' ' * (depth * GAP)}{key}: " + '{\n'\
            f"{result}\n{' ' * (depth * GAP)}" + '}'
    elif node_type == 'DELETED':
        return make_string(key, value, depth, '-')
    elif node_type == 'ADDED':
        return make_string(key, value, depth, '+')
    elif node_type == 'CHANGED':
        return f"{make_string(key, diff_tree.get('old_value'), depth, '-')}\n"\
               f"{make_string(key, diff_tree.get('new_value'), depth, '+')}"
    else:
        return f"{make_string(key, value, depth)}"




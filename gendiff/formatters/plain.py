from gendiff.errors import NodeTypeError


def processing_value(value):
    if value is None:
        return 'null'
    elif value is True or value is False:
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return f"{value}"
    return f"'{value}'"


def generate_plain_lines(diff_tree, parent=''):
    key = diff_tree.get('key')
    value = diff_tree.get('value')
    node_type = diff_tree.get('node_type')
    if node_type == 'root':
        children = diff_tree['children']
        lines = []
        for child in children:
            result = generate_plain_lines(child)
            if result is not None:
                lines.append(result)
        return '\n'.join(lines)
    elif node_type == 'NESTED':
        children = diff_tree['children']
        lines = []
        for child in children:
            result = generate_plain_lines(child, parent + f"{key}.")
            if result is not None:
                lines.append(result)
        result = '\n'.join(lines)
        return result
    elif node_type == 'ADDED':
        value = processing_value(value)
        return f"Property '{parent}{key}' was added with value: {value}"
    elif node_type == 'DELETED':
        return f"Property '{parent}{key}' was removed"
    elif node_type == 'CHANGED':
        old_value = processing_value(diff_tree.get('old_value'))
        new_value = processing_value(diff_tree.get('new_value'))
        return f"Property '{parent}{key}' was updated."\
               f" From {old_value} to {new_value}"
    elif node_type == 'SAME':
        pass
    else:
        raise NodeTypeError(f"Unexpected node type: '{node_type}'")

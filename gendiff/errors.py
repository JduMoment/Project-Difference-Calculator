class NodeTypeError(Exception):
    """Thrown when the node type is unknown"""
    pass


class FormatterError(Exception):
    """Throw when selected formatter absent"""
    pass


class FormatError(Exception):
    """Thrown when the file format is not supported."""
    pass

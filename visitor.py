import ast

ErrorType = tuple[int, int, str]
DEPRECATED_TYPING = ["Dict", "List", "Tuple", "Set"]
T100 = (
    "T100 found deprecated typing usage, "
    + "see more detail: https://www.python.org/dev/peps/pep-0585/"
)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[ErrorType] = []

    def visit_Assign(self, node: ast.Assign) -> None:  # noqa: N802
        self.errors.extend(check_deprecated_typing(node))
        self.generic_visit(node)


def check_deprecated_typing(node: ast.Assign) -> list[ErrorType]:
    errors: list[ErrorType] = []
    use_deprecated_typing = False
    if isinstance(node.value, ast.Subscript):
        use_deprecated_typing = _use_deprecated_typing(node.value)
    if use_deprecated_typing:
        errors.append((node.lineno, node.col_offset, T100))
    return errors


def _use_deprecated_typing(node: ast.Subscript) -> bool:
    assign_value = node.value
    if isinstance(assign_value, ast.Attribute):
        if assign_value.attr in DEPRECATED_TYPING:
            return True
        elif isinstance(assign_value, ast.Name):
            if assign_value.id in DEPRECATED_TYPING:
                return True
        return False

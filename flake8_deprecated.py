import ast
import importlib.metadata
import typing

import visitor


class Plugin:
    """Class defining plugin details."""

    name: str = __name__
    version: str = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self.tree = tree

    def run(
        self,
    ) -> typing.Generator[tuple[int, int, str, type[object]], None, None]:
        """Entry point for running a flake8 plugin."""
        node_visitor = visitor.Visitor()
        node_visitor.visit(self.tree)
        for line, col, msg in node_visitor.errors:
            yield line, col, msg, type(self)

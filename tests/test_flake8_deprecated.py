import ast
import flake8_deprecated
import pytest


def _get_plugin_results(line: str) -> set[str]:
    tree = ast.parse(line)
    plugin = flake8_deprecated.Plugin(tree)
    return {
        "{line_no}:{col} {msg}".format(line_no=line_no, col=col, msg=msg)
        for line_no, col, msg, _ in plugin.run()
    }


@pytest.mark.parametrize(
    "typing_content, expected_lint_error",
    [
        (
            "foo = list[int]\nbar = dict[str, str]",
            set(),
        ),
        (
            "foo = typing.List[int]\nbar = typing.Dict[str, str]",
            {
                (
                    (
                        "1:0 T100 found deprecated typing usage, see more "
                        + "detail: https://www.python.org/dev/peps/pep-0585/"
                    )
                ),
                (
                    "2:0 T100 found deprecated typing usage, see more detail: "
                    + "https://www.python.org/dev/peps/pep-0585/"
                ),
            },
        ),
    ],
)
def test_run(typing_content: str, expected_lint_error: set[str]) -> None:
    assert _get_plugin_results(typing_content) == expected_lint_error

# Flake8 Deprecated

A plugin to check using deprecated typing syntax.

## Installation

1. Clone this repo
```
git clone https://github.com/Shawnice/flake8_deprecated.git
```

2. Run the following command
```
python setup.py install
```

## Error codes

Code | Error Message
---- | ------------
T100 | T100 found deprecated typing usage

## Examples

```python
import typing

foo = list[int]  # OK
foo = typing.List[int]  # Error: T100 found deprecated typing usage
```

# Standard library
import pathlib

# Third-party
import setuptools

requires = [
    "flake8 > 3.0.0",
    "pytest",
]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="flake8_deprecated",
    license="MIT",
    version="0.1.0",
    description="A plugin to check using deprecated typing syntax.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="WXYLST",
    author_email="dev@example.com",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Flake8",
    ],
    py_modules=[
        "flake8_deprecated",
        "visitor",
    ],
    install_requires=requires,
    entry_points={
        "flake8.extension": [
            "ASY = flake8_async:Plugin",
        ],
    },
)

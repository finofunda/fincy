#!/usr/bin/env python

"""
Setup file for fincy package that uses setuptools and pyproject.toml
to generate wheel files, using modern packaging standards.

To build the package, use the build tools to generate the wheel files,
and to upload the package to PyPI, use the following command:

.. code-block:: bash

    python -m build --wheel
    python -m twine upload dist/*

The project is distributed under the terms of the MIT license. Check
project homepage https://github.com/finofunda/fincy for more details.
"""

import os
import tomli
import importlib

from pathlib import Path
from setuptools import setup, find_packages

def readfile(*filename : str, strip : bool = False) -> str:
    """
    Read a dynamic file by passing relative path to the file
    considering the current working directory. Standard IO error is
    raised if the file is not found.

    :type  filename: str
    :param filename: Relative path to the file parsed using
        ``os.path.join`` with list unpacking.

    :type  strip: bool
    :param strip: Strip the contents of the file if True using inbuilt
        string ``"my long string".strip()`` method.

    :rtype: str
    :return: Content of the file in string format, optionally stripped
        as per user requirement.
    """

    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, *filename)

    with open(filepath, "r", encoding = "utf-8") as f:
        content = f.read()

    return content.strip() if strip else content


def readtoml(tomlfile : str = "pyproject.toml") -> dict:
    """
    Read a pyproject.toml file content using ``tomlib`` library to
    get metadata classifiers. The file is read from the current
    directory and is a standard Python setup file.
    """

    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, tomlfile)

    with open(filepath, "rb") as f:
        content = tomli.load(f)

    return content


if __name__ == "__main__":
    pyproject = readtoml()
    projectmeta = pyproject.get("project", {})

    # get attribute for version name
    version = importlib.import_module(projectmeta["name"]).__version__
    print(version, projectmeta["name"])

    setup(
        name = projectmeta["name"],
        version = version,

        packages = find_packages(
            include = ["fincy", "fincy.*"],
            exclude = ["tests", "tests.*"]
        ),
    ) # execute setup tools on file run

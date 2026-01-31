<div align = "center">

# 💰 Financial Metrics Toolkit 💰

[![issues](https://img.shields.io/github/issues/finofunda/fincy?style=plastic)](https://github.com/finofunda/fincy/issues)
[![codeforks](https://img.shields.io/github/forks/finofunda/fincy?style=plastic)](https://github.com/finofunda/fincy/forks)
[![stargazers](https://img.shields.io/github/stars/finofunda/fincy?style=plastic)](https://github.com/finofunda/fincy/stargazers)
![codeversion](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&style=plastic)
[![Documentation Status](https://readthedocs.org/projects/fincy/badge/?version=latest)](https://fincy.readthedocs.io/en/latest/?badge=latest&style=plastic)
[![PyPI version](https://img.shields.io/pypi/v/fincy)](https://pypi.org/project/fincy/?style=plastic)

</div>

<div align = "justify">

Project **`fincy` 'FINancial efficienCY'** is a two-part project - (i) a Python library that can be seamlessly integrated to 
perform back-testing and other "AI" related stuffs, and (ii) a source control for TradingView's scripts that are hosted from
my [account](https://in.tradingview.com/u/ZenithClown/).

The Python package provides a lightweight and extensible Python toolkit for calculating financial metrics. Designed to work
**standalone** or integrate seamlessly with **external systems** through connectors, this project emphasizes clarity,
validation, and modular architecture. The package is available at [PyPI/fincy](https://pypi.org/project/fincy/).

## Getting Started

Python project is hosted at [GitHub/fincy](https://github.com/finofunda/fincy) and can be installed using Python Package
Index (PyPI), using the `pip` package manager as:

```shell
pip install fincy
```

### Installation from Source

To install the Python package `fincy` from source code, you need *git* client in your system, to clone the project in
your system as follows.

```shell
git clone https://github.com/finofunda/fincy.git
```

You can now directly install the package using the `pip` package manager from the `fincy` (same one where you found
this file after cloning the git repo) directory, execute:

```shell
pip install -r requirements.txt  # install the package dependencies
pip install .                    # install the package in the host machine
```

### Developer Installation

The documentation is compiled using Sphinx (MyST Parser) and hosted at ReadTheDocs. A developer requires additional packages
for documentation and can be installed (recommended to use a different environment) as:

```shell
cd docs # all documentations, configuration files, etc.
pip install -r requirements-docs.txt
```

### TradingView Scripts

TradingView's community hosting page provides a great interface for code documentation, release notes and other
essential things. For advanced concepts, statistical notes, Python implementations and other details please check the
[tradingview docs](https://fincy.readthedocs.io/en/latest/tradingview/index.html) under the project.

## LICENSE

The project is available under MIT License, while all the conents under the **`./tradingview/`** follows MPL 2.0 License by
default as per TradingView & PineScript policies.

## DISCLAIMER

The information and publications are not intended to be, and do not constitute, financial, investment, trading, or any other
form of advice or recommendations supplied or endorsed by the publisher or the creators of this script. Users are advised to
exercise their own judgment and seek professional advice before making any financial decisions.

</div>

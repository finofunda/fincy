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

A lightweight and extensible Python toolkit for calculating financial metrics. Designed to work **standalone** or integrate
seamlessly with **external systems** through connectors, this project emphasizes clarity, validation, and modular architecture.

## Getting Started

Project **`fincy`** is a two-part project - (i) a Python library that can be seamlessly integrated to perform back-testing and
other "AI" related stuffs, and (ii) a source control for TradingView's scripts that are hosted from my
[account](https://in.tradingview.com/u/ZenithClown/). Python project is hosted at
[GitHub/fincy](https://github.com/finofunda/fincy) and can be installed using Python Package Index (PyPI) as:

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

### TradingView Scripts

TradingView's community hosting page provides a great interface for code documentation, release notes and other
essential things. Check individual script notes as mention under [`./tradingview/README.md`](./tradingview/README.md)
file with additional details.

## LICENSE

The project is available under MIT License, while all the conents under the **`./tradingview/`** follows MPL 2.0 License by
default as per TradingView & PineScript policies.

</div>

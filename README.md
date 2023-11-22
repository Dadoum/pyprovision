# pyprovision

<center>Python bindings to Provision</center>

## Prerequisites

Tested with Python 3.8 and 3.10.

- Working D compiler
- DUB

If you are on a Windows, macOS or GNU/Linux computer, you can install one with one command:

```
curl -fsS https://dlang.org/install.sh | bash -s ldc
```

On other Linux distributions, you can probably find a recent compiler in your package manager (DMD, LDC or GDC, but a quite recent version is needed), and probably DUB, otherwise you can follow the instructions on [dub.pm](https://dub.pm/getting-started/install/).

Otherwise, just check the [D Programming language website](dlang.org) to have more detailed instructions.

## Installation

Just clone this repo and run:

```sh
$ python -m pip install .
```

It will then be installed in your python install and ready to be used!

If you encounter any issue whilst install the python package, please report it in issues, to help make this project better either in code or in documentation.

## Usage

See [example.py](example.py) to see how to make use of the library.
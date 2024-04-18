# FAST-OAD plugin template

## Introduction

This template repository is dedicated to the development of FAST-OAD models, possibly
packaged as a FAST-OAD plugin. These developments are explained in [FAST-OAD documentation](https://fast-oad.readthedocs.io/en/v1.4.2/documentation/custom_modules/index.html).

This README file explains how to use this template repository. Once your project
is set up, you are invited to erase this content and write your own README file,
suited to your project.

It is assumed that you know how to use [Git](https://git-scm.com), 
[Python](https://www.python.org) and [FAST-OAD](https://github.com/fast-aircraft-design/FAST-OAD).

This template is designed to use [Poetry](https://python-poetry.org) (version 1.4.2 or above)
for managing the development environment.
Instructions below assume you have it already installed. You may adapt them if you don't 
want to use Poetry.

_**Note**: In this document, any leading slash (`/`) in a path refers to project root._

## Setting up your project

After copying the content of this repository and initiating your own Git 
repository, you should take the following steps:

### Rename your plugin
- In `/src` folder, rename the `rename_me` folder. It will be the name of your 
  Python module.
- In `/pyproject.toml` file:
  - In `tool.poetry` section:
    - Use the new name of your Python module in the `packages` field.
    - Modify the `name` field with the name you want for your package
      (will be used in `pip install`, for instance).
  - In `tool.poetry.plugins."fastoad.plugins"`section:
    - Use the name of your Python module in the `packages` field (right-hand of 
      the equal sign).
    - Name your FAST-OAD plugin in the left-hand of the equal sign. Using the
      package name is recommended.

### Install your working environment
- Before creating your working environment, you may want to have a look at defined
  dependencies in `/pyproject.toml` file.
- Typing `poetry install` in your terminal will create a virtual environment and
  install all defined dependencies in it.

### Setup Git hooks
Simply run:
```bash
pre-commit install
```
(see below for more details)


## Local development tools

This template repository contains various configuration files to ease development.

Here are tools that will work in your local development environment.

### Pytest
[Pytest](https://docs.pytest.org/) is recommended for writing tests. The development environment
is set with code coverage tools.

**Pytest and its companions are configured in `/pyproject.toml` file.**

It is recommended to have unit tests in `tests` folders next to tested code.
Other kind of tests (integration, non-regression) should be in the `/tests` folder

Unit tests will be launched with simply:
```bash
pytest
```
To activate code coverage during unit testing, type:
```bash
pytest --cov
```

Other tests will be launched with
```bash
pytest tests
```

Jupyter notebooks can also be tested using:
```bash
pytest --nbval-lax -p no:python
```
_Note: with `--nbval-lax`, as said in nbval documentation, pytest "runs notebooks 
and checks for errors, but only compares the outputs of cells with a 
`#NBVAL_CHECK_OUTPUT` marker comment". If you want nbval to check all cell 
outputs against already saved ones, you need to use `--nbval` as option._ 

### Black
[Black](https://black.readthedocs.io/en/stable/?badge=stable) automates the code
formatting.

**Black is configured in `/pyproject.toml` file.**

Coupled with pre-commit (see below) and/or integrated with your IDE (see
[here](https://black.readthedocs.io/en/stable/integrations/editors.html)), it
automates all the code formatting, and it is sooo good.

_**Note to PyCharm users**: prefer the [file watcher](https://black.readthedocs.io/en/stable/integrations/editors.html#as-file-watcher), though the 2 other solutions can also be useful)_


### Flake8
[Flake8](https://flake8.pycqa.org/) is a tool for checking style guide, which helps
avoiding common coding mistakes.

**Flake8 is configured in `/.flake8` file.**

Coupled with pre-commit, it will check each line of code before it is committed.


### pre-commit
[pre-commit](https://pre-commit.com) is used to set up Git hooks for black and flake8.

**pre-commit is configured in `/.pre-commit-config.yaml` file.**

As already said, hooks are activated with:
```bash
pre-commit install
```

This operation has to be done only once in your development environment. Yet, 
you will have to do it again if the configuration file has been modified.


The installed hooks will interrupt the commit process if Black reformats a file or if
Flake8 detects a mistake.

In case of interruption, simply check the Git output messages and see what happened.

If the interruption comes from Black, doing the commit again should work. The 
interruption simply allows you to check the reformatted files before doing so.

If the interruption comes from Flake8, you will have to fix the identified
mistake before doing your commit again.


## Online tools

This section will be expanded in the future with settings for [Binder](https://mybinder.org), [Codacy](https://www.codacy.com), [CodeClimate](https://codeclimate.com), [Codecov](https://about.codecov.io) and [GitHub actions](https://github.com/features/actions).
# FAST-OAD plugin template

> **IMPORTANT**:
>
> For using this template, DO NOT clone it. Simply download its content as a zip file and unzip it into your new Git repository.

## Introduction

This template repository is dedicated to the development of FAST-OAD models, possibly packaged as a FAST-OAD plugin. These developments are explained in the [FAST-OAD documentation](<https://fast-oad.readthedocs.io/en/stable/documentation/custom_modules/index.html>).

This README file explains how to use this template repository. Once your project is set up, you are invited to erase this content and write your own README file, suited to your project.

It is assumed that you know how to use [Git](https://git-scm.com), [Python](https://www.python.org) and [FAST-OAD](https://github.com/fast-aircraft-design/FAST-OAD).

This template is designed to use [Poetry](https://python-poetry.org) (version 1.4.2 or above, but <2.0) for managing the development environment. Instructions below assume you have it already installed. You may adapt them if you don't want to use Poetry.

_**Note**: In this document, any leading slash (`/`) in a path refers to project root._

## Setting up your project

After copying the content of this repository and initiating your own Git repository, you should take the following steps:

### Rename your plugin

- In `/src` folder, rename the `rename_me` folder. It will be the name of your Python module.
- In `/pyproject.toml` file:
  - In `tool.poetry` section:
    - Use the new name of your Python module in the `packages` field.
    - Modify the `name` field with the name you want for your package (will be used in `pip install`, for instance).
  - In `tool.poetry.plugins."fastoad.plugins"`section:
    - Use the name of your Python module in the `packages` field (right-hand of the equal sign).
    - Name your FAST-OAD plugin in the left-hand of the equal sign. Using the package name is recommended.

### Install your working environment

- Before creating your working environment, you may want to have a look at defined dependencies in `/pyproject.toml` file.
- Typing `poetry install` in your terminal will create a virtual environment and install all defined dependencies in it.

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

[Pytest](https://docs.pytest.org/) is recommended for writing tests. The development environment is set with code coverage tools.

**Pytest and its companions are configured in `/pyproject.toml` file.**

It is recommended to have unit tests in `tests` folders next to tested code. Other kind of tests (integration, non-regression) should be in the `/tests` folder

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

_Note: with `--nbval-lax`, as said in nbval documentation, pytest "runs notebooks and checks for errors, but only compares the outputs of cells with a `#NBVAL_CHECK_OUTPUT` marker comment". If you want nbval to check all cell outputs against already saved ones, you need to use `--nbval` as option._

### Ruff

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) checks/corrects code style and automates the code formatting.

Kudos to [Black](https://black.readthedocs.io/en/stable) and [Flake8](https://flake8.pycqa.org/) that are very good tools. Yet, for a fresh start, Ruff seems the way to go, since it does the same job as these two, only much faster.

**Ruff is configured in `/pyproject.toml` file.**

Coupled with pre-commit (see below) and/or integrated with your IDE, it automates all the code formatting, and it is sooo good.

_**Note to PyCharm users**: there is a [ruff plugin](https://plugins.jetbrains.com/plugin/20574-ruff)._

### pre-commit
[pre-commit](https://pre-commit.com) is used to set up Git hooks for Ruff.

**pre-commit is configured in `/.pre-commit-config.yaml` file.**

As already said, hooks are activated with:

```bash
pre-commit install
```

This operation has to be done only once in your development environment. Yet, you will have to do it again if the configuration file has been modified.

The installed hooks will interrupt the commit process if Ruff reformats a file or if it detects a mistake.

In case of interruption, simply check the Git output messages and see what happened.

If the interruption comes from reformatting, doing the commit again should work. The interruption simply allows you to check the reformatted files before doing so.

If the interruption comes from Ruff check, you will have to fix the identified mistake before doing your commit again. Running `ruff check --fix` might help for the simplest problems.

## Importing the FAST-OAD model/plugin in another poetry package

As of now (14/04/2025), gitlab-dtis.onera does not accept SSH acces. So if you want to use your package in a different poetry package you can import it using http in your `pyproject.toml` file by using:

```toml
rename_me = { git = "http://gitlab-dtis.onera/designlab/fast-oad-models/add-real-path/rename_me.git" }
```

Make sure that your proxy is set correctly (remember, you want no proxy for http access to gitlab-dtis.onera). More information can be found [here](http://gitlab-dtis.onera/designlab/fast-oad-wiki/wikis/proxy-settings).


## Online tools

This section could be expanded in the future with settings for [Binder](https://mybinder.org), 
[Codacy](https://www.codacy.com), [CodeClimate](https://codeclimate.com), [Codecov](https://about.codecov.io) and [GitHub actions](https://github.com/features/actions).

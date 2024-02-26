# hatch-dependency-coversion

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-dependency-coversion.svg)](https://pypi.org/project/hatch-dependency-coversion)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-dependency-coversion.svg)](https://pypi.org/project/hatch-dependency-coversion)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

-----

This is a plugin for [Hatch](https://github.com/pypa/hatch) that allows you to rewrite the versions in selected dependency specifiers to be exactly the same as the current version of the project configured in `pyproject.toml`'s `[project]` table, requiring exact coversioning of those dependencies with the project.

This is useful for projects that are developed in lockstep but distributed as independent python packages rather than as subcomponents of the same namespace package. It is the equivalent of the following `setup.py`:

``` python
VERSION = '1.0.0'
setup(name='my-project', version=VERSION, install_requires=[f'my-dependency=={VERSION}'])
```

Minimal configuration is done in your `pyproject.toml` like this:

``` toml
[build-system]
# Since this is a plugin for hatchling, you must be using hatchling as your build backend
requires = ["hatchling", "hatch-dependency-coversion"]
build-backend = "hatchling.build"

[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    # 0.0.0 is chosen at random and will be overwritten
    "my-dependency==0.0.0"
]
[tool.hatch.metadata.hooks.dependency-coversion]
# this list contains the names of dependencies to override
override-versions-of = ["my-dependency"]
```

**Table of Contents**

- [Operation](#operation)
- [Use as a plugin](#plugin)
- [Configuration](#configuration)
- [License](#license)

## Operation

`hatch-dependency-coversion` is a metadata hook for `hatch`, or more specifically for `hatchling`, the PEP-508 build backend written by the `hatch` team. Whenever a package that uses `hatch-dependency-coversion` is built, `hatch-dependency-coversion` gets the chance to alter the list of dependencies the package will specify as required, and that `pip` and other installers or environment creators use to determine what dependencies to install.

Only those dependencies identified by name in the `tool.hatch.metadata.hooks.dependency-coversion.override-versions-of` list will have their versions overridden; nothing else will be touched.

Any PEP-440 version specifiers other than the version are left untouched; you can use `hatch-dependency-coversion` on dependencies that are optionally installed with markers (i.e. with `os_name == 'Windows'` or similar) and the markers will be preserved.


## Plugin

Ensure `hatch-dependency-coversion` is listed in the `build-system.requires` field in your `pyproject.toml`:

``` toml
[build-system]
requires = ["hatchling", "hatch-dependency-coversion"]
build-backend = "hatchling.build"
```

## Configuration

`hatch-dependency-coversion` is configured through `pyproject.toml` as a metadata hook in a similar way to other hatch plugins. Its plugin name is `dependency-coversion`:

``` toml
[tool.hatch.metadata.hooks.dependency-coversion]
override-versions-of = ["dependency1", "dependency2"]
```

The `override-versions-of` key is the only configuration that `hatch-dependency-coversion` takes. It is a list of strings, each of which should be the package name (the same thing you'd pass to `pip` or list in a dependency specifier) of one of the dependencies. Anything in here that is not in the top level `project.dependencies` key is ignored.

## License

`hatch-dependency-coversion` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

# hatch-vcs-tunable

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-git-version-tunable.svg)](https://pypi.org/project/hatch-vcs-tunable)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-git-version-tunable.svg)](https://pypi.org/project/hatch-vcs-tunable)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


-----

This is a plugin for [Hatch](https://github.com/pypa/hatch) that extends the plugin [hatch-vcs](https://github.com/ofek/hatch-vcs) to allow for overriding some config elements with environment variables.

The reason you might want to do this is if you have multiple release tracks for your package, or multiple contexts in which it is used, and want to give it different versions in those different contexts.

**Table of Contents**

- [Use as a plugin](#plugin)
- [Configuration](#Configuration)
- [License](#license)

## Plugin

Ensure `hatch-vcs-tunable` is listed in the `build-system.requires` field in your `pyproject.toml`:

```toml
[build-system]
requires = ["hatchling", "hatch-vcs-tunable"]
build-backend = "hatchling.build"
```

## Configuration

`hatch-vcs-tunable` can be configured either through `pyproject.toml`, using exactly the same configuration elements as `hatch-vcs` but with the plugin name `vcs-tunable`, or via environment variable overrides.

### `pyproject.toml`

Use the same configuration elements as `hatch-vcs`, but the plugin name `vcs-tunable`. For instance, to set the version file you would do:

``` toml
[tool.hatch.build.hooks.vcs-tunable]
version-file="_version.py"
```

### Environment

The environment variables should be specified as `ALL_CAPS_UNDERSCORE` versions of the pyproject settings, prefixed with `HATCH_VCS_TUNABLE_`. So for instance,
- `tag-pattern` can be specified as `HATCH_VCS_TUNABLE_TAG_PATTERN`
- `fallback-version` can be specified as `HATCH_VCS_TUNABLE_FALLBACK_VERSION`

#### `raw-options`

The value of the `raw-options` is passed directly to `setuptools_scm`. It may have multiple keyword arguments, which need both a name and a value, and the keywords may not be safe to put in the names of environment variables, so both the names and values are passed in the environment variable value. These should be passed as a string of `key-name=value` separated by `;`. For instance, to specify both `relative_to=..` and `version_file=/some/path`, you would do `HATCH_VCS_TUNABLE_RAW_OPTIONS="relative_to=..;version_file=/some/path"`.

If a setting is specified both in the environment and in `pyproject.toml`, the environment variable will take priority.

Environment variables that are specified as empty still exist, so if you do `HATCH_VCS_TUNABLE_FALLBACK_VERSION=  hatch build`, the fallback version will be the empty string. If you have one of these environment variables defined all the time and need to remove it, use `unset`.


## License

`hatch-git-version-tunable` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

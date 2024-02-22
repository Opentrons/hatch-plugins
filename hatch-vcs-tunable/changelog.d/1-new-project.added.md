# Added new project hatch-vcs-tunable

`hatch-vcs-tunable` is a plugin for [Hatch](https://github.com/pypa/hatch) that extends the plugin [hatch-vcs](https://github.com/ofek/hatch-vcs) to allow for overriding some config elements with environment variables. The reason you might want to do this is if you have multiple release tracks for your package, or multiple contexts in which it is used, and want to give it different versions in those different contexts.

To install `hatch-vcs-tunable`, list it as a PEP-517 dependency in your `pyproject.toml`'s `build-system` section alongside `hatchling` (you have to be using `hatchling` as your builder for this plugin to work):

```
[build-system]
requires = ["hatchling", "hatch-vcs-tunable"]
build-backend = "hatchling.build"
```

From there, you can configure the plugin exactly as you would configure `hatch-vcs`, except that
- The plugin name is `vcs-tunable`:
``` toml
[tool.hatch.build.hooks.vcs-tunable]
version-file="_version.py"
```

- You can override configuration from `pyproject.toml` using environment files at the time that you invoke your build frontend:

```bash
HATCH_VCS_TUNABLE_TAG_PATTERN='my-project-prefix@(?P<version>)' hatch build`
```

This allows for a system where you have different versions in different contexts. This can be useful if, for instance, you have different release tracks for a project, like an internal release and a public release, that have different versions.


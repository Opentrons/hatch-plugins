# Added new project hatch-dependency-coversion

`hatch-dependency-coversion` is a plugin for [Hatch](https://github.com/pypa/hatch) that that allows you to rewrite the versions in selected dependency specifiers to be exactly the same as the current version of the project configured in `pyproject.toml`'s `[project]` table, requiring exact coversioning of those dependencies with the project. This is useful for projects that are developed in lockstep but distributed as independent python packages rather than as subcomponents of the same namespace package.

To install `hatch-dependency-coversion`, list it as a PEP-517 dependency in your `pyproject.toml`'s `build-system` section alongside `hatchling` (you have to be using `hatchling` as your builder for this plugin to work):

```
[build-system]
requires = ["hatchling", "hatch-dependency-coversion"]
build-backend = "hatchling.build"
```

From there, you can configure the plugin by
- adding a `dynamic` entry to project metadata (containing an arbitrary string, such as the plugin name - the `dynamic` entry just needs to exist for hatch to call the plugin:
```toml
[project]
dynamic = ['hatch-dependency-coversion']
```
- The plugin name is `dependency-coversion`, and you set which dependency versions should be controlled with the config element `override-versions-of`, which should be an array of package names of dependencies from your `project.dependencies`:
``` toml

[project]
dependencies = ['my-favorite-package==0.1.0']

[tool.hatch.build.hooks.dependency-coversion]
override-versions-of=['my-favorite-package']
```

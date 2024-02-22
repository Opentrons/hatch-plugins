# Development Documentation

`hatch-vcs-tunable`is a python package developed using [Hatch](https://github.com/pypa/hatch) as its environment manager, task runner, and build frontend. Generally, any command that inspects or interacts with the package source is done through hatch.

## Contributing

Contributions should come through pull request. If done via a fork, a maintainer will run the CI checks after a quick review. Open source contributions are welcome! 

Pull requests should contain
- A descriptive title
   - that is prefixed with `hatch-vcs-tunable:`, since this repository has multiple packages
- A descriptive body that notes what the problem/missing feature is that the PR fixes and how the PR fixes it
- A note on how the PR should be tested, if testing is required, and descriptions of how you tested it
- A news fragment in `changelog.d` that adheres to [towncrier news fragment format](https://towncrier.readthedocs.io/en/stable/tutorial.html#creating-news-fragments) describing your change
- If you're not already in it and you want to be, an addition of yourself to CONTRIBUTORS.md

## Linting/formatting/typechecking

Static analysis tools are run from the default hatch environment. Typechecking is via [mypy](http://mypy-lang.org/), linting and formatting is via [ruff](https://github.com/astral-sh/ruff). You can run these commands with `hatch run` without further qualification:
- Typecheck: `hatch run check`
- Format: `hatch run format`
- Lint: `hatch run lint`
  - Auto lint fixes: `hatch run lint --fix`
  
These all must pass in CI before a PR can be merged.
  
## Tests

Tests are defined both in the default environment (in which case they will run just in whatever python environment and dependency set you happen to have installed) and in a special `test` environment endowed with matrix definitions for multiple python versions and multiple versions of the `hatch-vcs` plugin that `hatch-vcs-tunable` extends.

- Run quick tests: `hatch run test`
- Run full test matrix: `hatch run test:test`

Tests must pass in CI before a PR can be merged.

## Maintenance and Releasing

Changelogs are generated using [towncrier](https://towncrier.readthedocs.io/en/stable/index.html). When opening a PR that has a newsworthy change, that PR should include a news fragment in `changelog.d`. Changelog generation happens during the release flow, which is automated via github actions that can be run by project maintainers.



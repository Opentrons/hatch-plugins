# (Opentrons) Hatch Plugins

This repository contains two hatch plugins used for python package builds in https://github.com/Opentrons/opentrons.

- `hatch-git-version-tunable` is a plugin that can define dynamic versions from git tags, but with the ability to specify at build time what tag prefix to use. This requires its own plugin because it's an unusual need; we use this workflow for having two separate release tracks for the same software.
- `hatch-dependency-coversion` is a plugin that can rewrite dependency metadata for a package so that some specific dependency or set of dependencies requires an exact coversion of the top level package. This is also an uncommon workflow because few people develop many independent python packages in the same monorepo.

Since this repo is also sort of a monorepo, there's not much going on in this top level. See the directories for each package for more information.

Issues are managed in github issues in this repository. Open source contributions are welcome!

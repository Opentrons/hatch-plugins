# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

"""A metadata hook for hatchling that can force dependencies to be coversioned."""
from __future__ import annotations
from typing import Any

from packaging.requirements import Requirement, SpecifierSet

from hatchling.metadata.plugin.interface import MetadataHookInterface
from hatch_dependency_coversion.const import PLUGIN_NAME as _PLUGIN_NAME


class DependencyCoversionMetadataHook(MetadataHookInterface):
    PLUGIN_NAME = _PLUGIN_NAME

    def _maybe_update_dep(
        self, depspec: str, version: str, which_dependencies: list[str]
    ) -> str:
        requirement = Requirement(depspec)
        if requirement.name not in which_dependencies:
            return depspec
        requirement.specifier = SpecifierSet(f"=={version}")
        return str(requirement)

    def _update_dependency_versions(
        self,
        dependencies_metadata: list[str],
        version: str,
        which_dependencies: list[str],
    ) -> list[str]:
        """Do the actual dependency update"""
        return [
            self._maybe_update_dep(depspec, version, which_dependencies)
            for depspec in dependencies_metadata
        ]

    def update(self, metadata: dict[str, Any]) -> None:
        """Update metadata for coversioning."""
        metadata["dependencies"] = self._update_dependency_versions(
            metadata.get("dependencies", []),
            metadata["version"],
            self.config.get("override-versions-of", []),
        )

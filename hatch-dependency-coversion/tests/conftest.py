# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from textwrap import dedent
from pathlib import Path
import pytest


@pytest.fixture
def static_requirements() -> list[str]:
    return [
        "dependency1",
        "dependency2==10.10.2",
        "dependency3>=0.2.81; os_name == 'Windows'",
    ]


@pytest.fixture
def unconfigured_project(tmp_path: Path, static_requirements: list[str]) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "unconfigured-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        """
        )
    )
    (tmp_path / "unconfigured_project").mkdir()
    (tmp_path / "unconfigured_project" / "__init__.py").write_text("")
    return tmp_path


@pytest.fixture
def requests_zero_coversions_project(
    tmp_path: Path, static_requirements: list[str]
) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "zero-coversions-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        override-versions-of=[]
        """
        )
    )
    (tmp_path / "zero_coversions_project").mkdir()
    (tmp_path / "zero_coversions_project" / "__init__.py").write_text("")
    return tmp_path


@pytest.fixture
def requests_coversion_of_open_version_project(
    tmp_path: Path, static_requirements: list[str]
) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "coversion-of-open-version-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        override-versions-of=["dependency1"]
        """
        )
    )
    (tmp_path / "coversion_of_open_version_project").mkdir()
    (tmp_path / "coversion_of_open_version_project" / "__init__.py").write_text("")
    return tmp_path


@pytest.fixture
def requests_coversion_of_specified_version_project(
    tmp_path: Path, static_requirements: list[str]
) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "coversion-of-specified-version-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        override-versions-of=["dependency2"]
        """
        )
    )
    (tmp_path / "coversion_of_specified_version_project").mkdir()
    (tmp_path / "coversion_of_specified_version_project" / "__init__.py").write_text("")
    return tmp_path


@pytest.fixture
def requests_coversion_of_marked_version_project(
    tmp_path: Path, static_requirements: list[str]
) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "coversion-of-marked-version-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        override-versions-of=["dependency3"]
        """
        )
    )
    (tmp_path / "coversion_of_marked_version_project").mkdir()
    (tmp_path / "coversion_of_marked_version_project" / "__init__.py").write_text("")
    return tmp_path


@pytest.fixture
def requests_multiple_project(tmp_path: Path, static_requirements: list[str]) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        dedent(
            f"""
        [build-system]
        requires = ["hatchling", "hatch-dependency-coversion"]
        build-backend = "hatchling.build"
        [project]
        name = "coversion-of-multiple-project"
        version = "0.1.0"
        dependencies = [{','.join([f'"{requirement}"' for requirement in static_requirements])}]
        [tool.hatch.metadata.hooks.dependency-coversion]
        override-versions-of=["dependency2", "dependency1", "dependency3"]
        """
        )
    )
    (tmp_path / "coversion_of_multiple_project").mkdir()
    (tmp_path / "coversion_of_multiple_project" / "__init__.py").write_text("")
    return tmp_path

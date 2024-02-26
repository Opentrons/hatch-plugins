from __future__ import annotations
from pathlib import Path
import pkginfo
from .utils import build_wheel


def test_unconfigured_project_changes_nothing(
    unconfigured_project: Path, static_requirements: list[str]
) -> None:
    wheelpath = build_wheel(unconfigured_project)
    dist_metadata = pkginfo.Wheel(str(wheelpath))
    requires = dist_metadata.requires_dist
    assert requires == static_requirements


def test_zero_requested_coversions_changes_nothing(
    requests_zero_coversions_project: Path, static_requirements: list[str]
) -> None:
    wheelpath = build_wheel(requests_zero_coversions_project)
    dist_metadata = pkginfo.Wheel(str(wheelpath))
    requires = dist_metadata.requires_dist
    assert requires == static_requirements


def test_coversion_of_open_version_applies(
    requests_coversion_of_open_version_project: Path, static_requirements: list[str]
) -> None:
    wheelpath = build_wheel(requests_coversion_of_open_version_project)
    dist_metadata = pkginfo.Wheel(str(wheelpath))
    requires = dist_metadata.requires_dist
    assert sorted(requires) == ["dependency1==0.1.0"] + static_requirements[1:]


def test_coversion_of_specified_version_applies(
    requests_coversion_of_specified_version_project: Path,
    static_requirements: list[str],
) -> None:
    wheelpath = build_wheel(requests_coversion_of_specified_version_project)
    dist_metadata = pkginfo.Wheel(str(wheelpath))
    requires = dist_metadata.requires_dist
    assert (
        sorted(requires)
        == [static_requirements[0]] + ["dependency2==0.1.0"] + static_requirements[2:]
    )


def test_coversion_of_marked_version_applies(
    requests_coversion_of_marked_version_project: Path, static_requirements: list[str]
) -> None:
    wheelpath = build_wheel(requests_coversion_of_marked_version_project)
    dist_metadata = pkginfo.Wheel(str(wheelpath))
    requires = dist_metadata.requires_dist
    assert sorted(requires) == static_requirements[:2] + [
        "dependency3==0.1.0; os_name == 'Windows'"
    ]

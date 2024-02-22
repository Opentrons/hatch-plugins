# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations
import pytest

from hatch_vcs_tunable.version_source import TunableVCSVersionSource


@pytest.fixture
def subject() -> TunableVCSVersionSource:
    return TunableVCSVersionSource(
        "some-root",
        {
            "tag-pattern": "upstream-tag-pattern",
            "fallback-version": "upstream-fallback-version",
            "raw-options": {
                "upstream-key-1": "upstream-val-1",
                "upstream-key-2": "upstream-val-2",
            },
        },
    )


def test_config_tag_pattern_uses_environ(
    monkeypatch: pytest.MonkeyPatch, subject: TunableVCSVersionSource
) -> None:
    monkeypatch.setenv("HATCH_VCS_TUNABLE_TAG_PATTERN", "my-tag-pattern")
    assert subject.config_tag_pattern == "my-tag-pattern"


def test_config_tag_pattern_falls_back(
    subject: TunableVCSVersionSource,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("HATCH_VCS_TUNABLE_TAG_PATTERN", raising=False)
    assert subject.config_tag_pattern == "upstream-tag-pattern"


def test_config_fallback_version_uses_environ(
    subject: TunableVCSVersionSource,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("HATCH_VCS_TUNABLE_FALLBACK_VERSION", "my-fallback-version")
    assert subject.config_fallback_version == "my-fallback-version"


def test_config_fallback_version_falls_back(
    subject: TunableVCSVersionSource,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("HATCH_VCS_TUNABLE_FALLBACK_VERSION", raising=False)
    assert subject.config_fallback_version == "upstream-fallback-version"


def test_config_raw_options_falls_back(
    subject: TunableVCSVersionSource, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("HATCH_VCS_TUNABLE_RAW_OPTIONS", raising=False)
    assert subject.config_raw_options == {
        "upstream-key-1": "upstream-val-1",
        "upstream-key-2": "upstream-val-2",
    }


def test_config_raw_options_handles_simple(
    subject: TunableVCSVersionSource, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv(
        "HATCH_VCS_TUNABLE_RAW_OPTIONS", "my-key-1=my_val-1;my/key_2=my!val\\2"
    )
    assert subject.config_raw_options == {
        "upstream-key-1": "upstream-val-1",
        "upstream-key-2": "upstream-val-2",
        "my-key-1": "my_val-1",
        "my/key_2": "my!val\\2",
    }


def test_config_raw_options_handles_internal_semis(
    subject: TunableVCSVersionSource, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv(
        "HATCH_VCS_TUNABLE_RAW_OPTIONS", "my-key-1=my;val;1;my-key-2=my;val;2"
    )
    assert subject.config_raw_options == {
        "upstream-key-1": "upstream-val-1",
        "upstream-key-2": "upstream-val-2",
        "my-key-1": "my;val;1",
        "my-key-2": "my;val;2",
    }


def test_config_raw_options_handles_internal_equals(
    subject: TunableVCSVersionSource, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv(
        "HATCH_VCS_TUNABLE_RAW_OPTIONS", "my-key-1=my=val1;my-key-2===my=val2"
    )
    assert subject.config_raw_options == {
        "upstream-key-1": "upstream-val-1",
        "upstream-key-2": "upstream-val-2",
        "my-key-1": "my=val1",
        "my-key-2": "==my=val2",
    }

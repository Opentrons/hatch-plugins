# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0
"""A version source extending hatch_vcs with the ability to set configuration from the environment."""
from __future__ import annotations
from os import environ
from collections import deque
from typing import Iterable

from .const import (
    TAG_PATTERN_ENVIRON_NAME,
    FALLBACK_VERSION_ENVIRON_NAME,
    PLUGIN_NAME as _PLUGIN_NAME,
    RAW_OPTIONS_ENVIRON_NAME,
)

from hatch_vcs.version_source import VCSVersionSource  # type: ignore[import-untyped]


def _collapse_semis(parts: Iterable[str]) -> list[str]:
    ret: list[list[str]] = []
    remaining = deque(parts)
    try:
        ret.append([remaining.popleft()])
    except IndexError:
        return []
    while remaining:
        try:
            top = remaining.popleft()
            if "=" not in top:
                ret[-1].append(top)
            else:
                ret.append([top])
        except IndexError:
            break
    return [";".join(parts) for parts in ret]


def _opts_from_pairs(optionpairs: list[str]) -> list[tuple[str, str]]:
    return [_opt_from_pair(pair) for pair in optionpairs]


def _opt_from_pair(optionpair: str) -> tuple[str, str]:
    key, *valparts = optionpair.split("=")
    return (key, "=".join(valparts))


def to_dict(optionpairs: list[str]) -> dict[str, str]:
    return {key: val for key, val in _opts_from_pairs(optionpairs)}


def _options_from_environ(envstr: str) -> dict[str, str]:
    return to_dict(_collapse_semis(part for part in envstr.split(";") if part))


class TunableVCSVersionSource(VCSVersionSource):
    """An extension of hatch_vcs VCSVersionSource that allows overriding the tag prefix."""

    PLUGIN_NAME = _PLUGIN_NAME

    def __init__(self, root: str, config: dict, *args, **kwargs) -> None:
        super().__init__(root, config, *args, **kwargs)

    @property
    def config_tag_pattern(self) -> str:
        from_env = environ.get(TAG_PATTERN_ENVIRON_NAME, None)
        if from_env is not None:
            return from_env
        return super().config_tag_pattern

    @property
    def config_fallback_version(self) -> str:
        from_env = environ.get(FALLBACK_VERSION_ENVIRON_NAME, None)
        if from_env is not None:
            return from_env
        return super().config_fallback_version

    @property
    def config_raw_options(self) -> dict[str, str]:
        config_options = super().config_raw_options
        from_env = environ.get(RAW_OPTIONS_ENVIRON_NAME, None)
        if from_env is not None:
            config_options.update(_options_from_environ(from_env))
        return config_options

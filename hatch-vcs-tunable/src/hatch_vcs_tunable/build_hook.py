# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

"""A re-export of hatch_vcs that must be provided for full plugin functionality."""

from hatch_vcs.build_hook import VCSBuildHook  # type: ignore[import-untyped]
from hatch_vcs_tunable.const import PLUGIN_NAME as _PLUGIN_NAME


class TunableVCSBuildHook(VCSBuildHook):
    PLUGIN_NAME = _PLUGIN_NAME

# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

"""
Registers hatch hooks overriding and extending those from hatch_vcs.
"""

from hatchling.plugin import hookimpl
from hatch_vcs_tunable.version_source import TunableVCSVersionSource
from hatch_vcs_tunable.build_hook import TunableVCSBuildHook
from hatch_vcs_tunable.metadata_hook import TunableVCSMetadataHook


@hookimpl
def hatch_register_version_source():
    return TunableVCSVersionSource


@hookimpl
def hatch_register_build_hook():
    return TunableVCSBuildHook


@hookimpl
def hatch_register_metadata_hook():
    return TunableVCSMetadataHook

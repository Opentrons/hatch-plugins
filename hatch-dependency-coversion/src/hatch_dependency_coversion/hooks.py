# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

"""Registers a hatch metadata hook for altering dependency versions."""

from hatchling.plugin import hookimpl
from .metadata_hook import DependencyCoversionMetadataHook


@hookimpl
def hatch_register_metadata_hook():
    return DependencyCoversionMetadataHook

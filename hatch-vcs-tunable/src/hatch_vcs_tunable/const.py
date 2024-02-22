# SPDX-FileCopyrightText: 2024-present Opentrons Engineering <engineering@opentrons.com>
#
# SPDX-License-Identifier: Apache-2.0

from typing import Final

PLUGIN_NAME: Final = "vcs-tunable"

ENVIRON_PREFIX: Final = "HATCH_VCS_TUNABLE_"
TAG_PATTERN_ENVIRON_NAME: Final = ENVIRON_PREFIX + "TAG_PATTERN"
FALLBACK_VERSION_ENVIRON_NAME: Final = ENVIRON_PREFIX + "FALLBACK_VERSION"
RAW_OPTIONS_ENVIRON_NAME: Final = ENVIRON_PREFIX + "RAW_OPTIONS"

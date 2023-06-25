# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ChannelSectionContentDetails(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChannelSectionContentDetails - a model defined in OpenAPI

        channels: The channels of this ChannelSectionContentDetails [Optional].
        playlists: The playlists of this ChannelSectionContentDetails [Optional].
    """

    channels: Optional[List[str]] = None
    playlists: Optional[List[str]] = None

ChannelSectionContentDetails.update_forward_refs()

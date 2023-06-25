# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ChannelBannerResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChannelBannerResource - a model defined in OpenAPI

        etag: The etag of this ChannelBannerResource [Optional].
        kind: The kind of this ChannelBannerResource [Optional].
        url: The url of this ChannelBannerResource [Optional].
    """

    etag: Optional[str] = None
    kind: Optional[str] = None
    url: Optional[str] = None

ChannelBannerResource.update_forward_refs()

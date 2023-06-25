# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class LocalizedString(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LocalizedString - a model defined in OpenAPI

        language: The language of this LocalizedString [Optional].
        value: The value of this LocalizedString [Optional].
    """

    language: Optional[str] = None
    value: Optional[str] = None

LocalizedString.update_forward_refs()

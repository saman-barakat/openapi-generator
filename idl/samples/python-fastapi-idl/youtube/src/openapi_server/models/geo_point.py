# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class GeoPoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GeoPoint - a model defined in OpenAPI

        altitude: The altitude of this GeoPoint [Optional].
        latitude: The latitude of this GeoPoint [Optional].
        longitude: The longitude of this GeoPoint [Optional].
    """

    altitude: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

GeoPoint.update_forward_refs()

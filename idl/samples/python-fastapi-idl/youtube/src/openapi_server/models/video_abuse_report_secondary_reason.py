# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class VideoAbuseReportSecondaryReason(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VideoAbuseReportSecondaryReason - a model defined in OpenAPI

        id: The id of this VideoAbuseReportSecondaryReason [Optional].
        label: The label of this VideoAbuseReportSecondaryReason [Optional].
    """

    id: Optional[str] = None
    label: Optional[str] = None

VideoAbuseReportSecondaryReason.update_forward_refs()

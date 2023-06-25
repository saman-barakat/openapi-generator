# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class VideoSuggestionsTagSuggestion(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VideoSuggestionsTagSuggestion - a model defined in OpenAPI

        category_restricts: The category_restricts of this VideoSuggestionsTagSuggestion [Optional].
        tag: The tag of this VideoSuggestionsTagSuggestion [Optional].
    """

    category_restricts: Optional[List[str]] = None
    tag: Optional[str] = None

VideoSuggestionsTagSuggestion.update_forward_refs()

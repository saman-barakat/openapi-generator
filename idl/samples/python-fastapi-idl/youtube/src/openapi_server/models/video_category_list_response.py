# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.page_info import PageInfo
from openapi_server.models.video_category import VideoCategory


class VideoCategoryListResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VideoCategoryListResponse - a model defined in OpenAPI

        etag: The etag of this VideoCategoryListResponse [Optional].
        event_id: The event_id of this VideoCategoryListResponse [Optional].
        items: The items of this VideoCategoryListResponse [Optional].
        kind: The kind of this VideoCategoryListResponse [Optional].
        next_page_token: The next_page_token of this VideoCategoryListResponse [Optional].
        page_info: The page_info of this VideoCategoryListResponse [Optional].
        prev_page_token: The prev_page_token of this VideoCategoryListResponse [Optional].
        token_pagination: The token_pagination of this VideoCategoryListResponse [Optional].
        visitor_id: The visitor_id of this VideoCategoryListResponse [Optional].
    """

    etag: Optional[str] = None
    event_id: Optional[str] = None
    items: Optional[List[VideoCategory]] = None
    kind: Optional[str] = None
    next_page_token: Optional[str] = None
    page_info: Optional[PageInfo] = None
    prev_page_token: Optional[str] = None
    token_pagination: Optional[Dict[str, Any]] = None
    visitor_id: Optional[str] = None

VideoCategoryListResponse.update_forward_refs()

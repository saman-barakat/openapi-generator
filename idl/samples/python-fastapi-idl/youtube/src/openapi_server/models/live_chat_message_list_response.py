# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.live_chat_message import LiveChatMessage
from openapi_server.models.page_info import PageInfo


class LiveChatMessageListResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LiveChatMessageListResponse - a model defined in OpenAPI

        etag: The etag of this LiveChatMessageListResponse [Optional].
        event_id: The event_id of this LiveChatMessageListResponse [Optional].
        items: The items of this LiveChatMessageListResponse [Optional].
        kind: The kind of this LiveChatMessageListResponse [Optional].
        next_page_token: The next_page_token of this LiveChatMessageListResponse [Optional].
        offline_at: The offline_at of this LiveChatMessageListResponse [Optional].
        page_info: The page_info of this LiveChatMessageListResponse [Optional].
        polling_interval_millis: The polling_interval_millis of this LiveChatMessageListResponse [Optional].
        token_pagination: The token_pagination of this LiveChatMessageListResponse [Optional].
        visitor_id: The visitor_id of this LiveChatMessageListResponse [Optional].
    """

    etag: Optional[str] = None
    event_id: Optional[str] = None
    items: Optional[List[LiveChatMessage]] = None
    kind: Optional[str] = None
    next_page_token: Optional[str] = None
    offline_at: Optional[datetime] = None
    page_info: Optional[PageInfo] = None
    polling_interval_millis: Optional[int] = None
    token_pagination: Optional[Dict[str, Any]] = None
    visitor_id: Optional[str] = None

LiveChatMessageListResponse.update_forward_refs()

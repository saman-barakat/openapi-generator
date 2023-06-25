# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.video_age_gating import VideoAgeGating
from openapi_server.models.video_content_details import VideoContentDetails
from openapi_server.models.video_file_details import VideoFileDetails
from openapi_server.models.video_live_streaming_details import VideoLiveStreamingDetails
from openapi_server.models.video_localization import VideoLocalization
from openapi_server.models.video_monetization_details import VideoMonetizationDetails
from openapi_server.models.video_player import VideoPlayer
from openapi_server.models.video_processing_details import VideoProcessingDetails
from openapi_server.models.video_recording_details import VideoRecordingDetails
from openapi_server.models.video_snippet import VideoSnippet
from openapi_server.models.video_statistics import VideoStatistics
from openapi_server.models.video_status import VideoStatus
from openapi_server.models.video_suggestions import VideoSuggestions
from openapi_server.models.video_topic_details import VideoTopicDetails


class Video(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Video - a model defined in OpenAPI

        age_gating: The age_gating of this Video [Optional].
        content_details: The content_details of this Video [Optional].
        etag: The etag of this Video [Optional].
        file_details: The file_details of this Video [Optional].
        id: The id of this Video [Optional].
        kind: The kind of this Video [Optional].
        live_streaming_details: The live_streaming_details of this Video [Optional].
        localizations: The localizations of this Video [Optional].
        monetization_details: The monetization_details of this Video [Optional].
        player: The player of this Video [Optional].
        processing_details: The processing_details of this Video [Optional].
        project_details: The project_details of this Video [Optional].
        recording_details: The recording_details of this Video [Optional].
        snippet: The snippet of this Video [Optional].
        statistics: The statistics of this Video [Optional].
        status: The status of this Video [Optional].
        suggestions: The suggestions of this Video [Optional].
        topic_details: The topic_details of this Video [Optional].
    """

    age_gating: Optional[VideoAgeGating] = None
    content_details: Optional[VideoContentDetails] = None
    etag: Optional[str] = None
    file_details: Optional[VideoFileDetails] = None
    id: Optional[str] = None
    kind: Optional[str] = None
    live_streaming_details: Optional[VideoLiveStreamingDetails] = None
    localizations: Optional[Dict[str, VideoLocalization]] = None
    monetization_details: Optional[VideoMonetizationDetails] = None
    player: Optional[VideoPlayer] = None
    processing_details: Optional[VideoProcessingDetails] = None
    project_details: Optional[Dict[str, Any]] = None
    recording_details: Optional[VideoRecordingDetails] = None
    snippet: Optional[VideoSnippet] = None
    statistics: Optional[VideoStatistics] = None
    status: Optional[VideoStatus] = None
    suggestions: Optional[VideoSuggestions] = None
    topic_details: Optional[VideoTopicDetails] = None

Video.update_forward_refs()

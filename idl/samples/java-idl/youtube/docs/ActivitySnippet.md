

# ActivitySnippet

Basic details about an activity, including title, description, thumbnails, activity type and group. Next ID: 12

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel associated with the activity. |  [optional]
**channelTitle** | **String** | Channel title for the channel responsible for this activity |  [optional]
**description** | **String** | The description of the resource primarily associated with the activity. @mutable youtube.activities.insert |  [optional]
**groupId** | **String** | The group ID associated with the activity. A group ID identifies user events that are associated with the same user and resource. For example, if a user rates a video and marks the same video as a favorite, the entries for those events would have the same group ID in the user&#39;s activity feed. In your user interface, you can avoid repetition by grouping events with the same groupId value. |  [optional]
**publishedAt** | **OffsetDateTime** | The date and time that the video was uploaded. |  [optional]
**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  |  [optional]
**title** | **String** | The title of the resource primarily associated with the activity. |  [optional]
**type** | [**TypeEnum**](#TypeEnum) | The type of activity that the resource describes. |  [optional]



## Enum: TypeEnum

Name | Value
---- | -----
TYPEUNSPECIFIED | &quot;typeUnspecified&quot;
UPLOAD | &quot;upload&quot;
LIKE | &quot;like&quot;
FAVORITE | &quot;favorite&quot;
COMMENT | &quot;comment&quot;
SUBSCRIPTION | &quot;subscription&quot;
PLAYLISTITEM | &quot;playlistItem&quot;
RECOMMENDATION | &quot;recommendation&quot;
BULLETIN | &quot;bulletin&quot;
SOCIAL | &quot;social&quot;
CHANNELITEM | &quot;channelItem&quot;
PROMOTEDITEM | &quot;promotedItem&quot;






# VideoAgeGating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alcoholContent** | **Boolean** | Indicates whether or not the video has alcoholic beverage content. Only users of legal purchasing age in a particular country, as identified by ICAP, can view the content. |  [optional]
**restricted** | **Boolean** | Age-restricted trailers. For redband trailers and adult-rated video-games. Only users aged 18+ can view the content. The the field is true the content is restricted to viewers aged 18+. Otherwise The field won&#39;t be present. |  [optional]
**videoGameRating** | [**VideoGameRatingEnum**](#VideoGameRatingEnum) | Video game rating, if any. |  [optional]



## Enum: VideoGameRatingEnum

Name | Value
---- | -----
ANYONE | &quot;anyone&quot;
M15PLUS | &quot;m15Plus&quot;
M16PLUS | &quot;m16Plus&quot;
M17PLUS | &quot;m17Plus&quot;




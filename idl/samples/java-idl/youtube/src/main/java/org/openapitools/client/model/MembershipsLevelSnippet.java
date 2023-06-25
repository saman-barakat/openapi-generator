/*
 * YouTube Data API v3
 * The YouTube Data API v3 is an API that provides access to YouTube data, such as videos, playlists, and channels.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.LevelDetails;

/**
 * MembershipsLevelSnippet
 */
@javax.annotation.Generated(value = "com.us.idl.javaidl.JavaIDLCodegen", date = "2021-08-24T20:55:04.712703200+02:00[Europe/Paris]")
public class MembershipsLevelSnippet {
  public static final String SERIALIZED_NAME_CREATOR_CHANNEL_ID = "creatorChannelId";
  @SerializedName(SERIALIZED_NAME_CREATOR_CHANNEL_ID)
  private String creatorChannelId;

  public static final String SERIALIZED_NAME_LEVEL_DETAILS = "levelDetails";
  @SerializedName(SERIALIZED_NAME_LEVEL_DETAILS)
  private LevelDetails levelDetails;


  public MembershipsLevelSnippet creatorChannelId(String creatorChannelId) {
    
    this.creatorChannelId = creatorChannelId;
    return this;
  }

   /**
   * The id of the channel that&#39;s offering channel memberships.
   * @return creatorChannelId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The id of the channel that's offering channel memberships.")

  public String getCreatorChannelId() {
    return creatorChannelId;
  }


  public void setCreatorChannelId(String creatorChannelId) {
    this.creatorChannelId = creatorChannelId;
  }


  public MembershipsLevelSnippet levelDetails(LevelDetails levelDetails) {
    
    this.levelDetails = levelDetails;
    return this;
  }

   /**
   * Get levelDetails
   * @return levelDetails
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public LevelDetails getLevelDetails() {
    return levelDetails;
  }


  public void setLevelDetails(LevelDetails levelDetails) {
    this.levelDetails = levelDetails;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MembershipsLevelSnippet membershipsLevelSnippet = (MembershipsLevelSnippet) o;
    return Objects.equals(this.creatorChannelId, membershipsLevelSnippet.creatorChannelId) &&
        Objects.equals(this.levelDetails, membershipsLevelSnippet.levelDetails);
  }

  @Override
  public int hashCode() {
    return Objects.hash(creatorChannelId, levelDetails);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MembershipsLevelSnippet {\n");
    sb.append("    creatorChannelId: ").append(toIndentedString(creatorChannelId)).append("\n");
    sb.append("    levelDetails: ").append(toIndentedString(levelDetails)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}


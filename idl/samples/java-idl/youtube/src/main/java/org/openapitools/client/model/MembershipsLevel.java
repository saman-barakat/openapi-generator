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
import org.openapitools.client.model.MembershipsLevelSnippet;

/**
 * A *membershipsLevel* resource represents an offer made by YouTube creators for their fans. Users can become members of the channel by joining one of the available levels. They will provide recurring monetary support and receives special benefits.
 */
@ApiModel(description = "A *membershipsLevel* resource represents an offer made by YouTube creators for their fans. Users can become members of the channel by joining one of the available levels. They will provide recurring monetary support and receives special benefits.")
@javax.annotation.Generated(value = "com.us.idl.javaidl.JavaIDLCodegen", date = "2021-08-24T20:55:04.712703200+02:00[Europe/Paris]")
public class MembershipsLevel {
  public static final String SERIALIZED_NAME_ETAG = "etag";
  @SerializedName(SERIALIZED_NAME_ETAG)
  private String etag;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private String kind = "youtube#membershipsLevel";

  public static final String SERIALIZED_NAME_SNIPPET = "snippet";
  @SerializedName(SERIALIZED_NAME_SNIPPET)
  private MembershipsLevelSnippet snippet;


  public MembershipsLevel etag(String etag) {
    
    this.etag = etag;
    return this;
  }

   /**
   * Etag of this resource.
   * @return etag
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Etag of this resource.")

  public String getEtag() {
    return etag;
  }


  public void setEtag(String etag) {
    this.etag = etag;
  }


  public MembershipsLevel id(String id) {
    
    this.id = id;
    return this;
  }

   /**
   * The ID that YouTube assigns to uniquely identify the memberships level.
   * @return id
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The ID that YouTube assigns to uniquely identify the memberships level.")

  public String getId() {
    return id;
  }


  public void setId(String id) {
    this.id = id;
  }


  public MembershipsLevel kind(String kind) {
    
    this.kind = kind;
    return this;
  }

   /**
   * Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#membershipsLevelListResponse\&quot;.
   * @return kind
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Identifies what kind of resource this is. Value: the fixed string \"youtube#membershipsLevelListResponse\".")

  public String getKind() {
    return kind;
  }


  public void setKind(String kind) {
    this.kind = kind;
  }


  public MembershipsLevel snippet(MembershipsLevelSnippet snippet) {
    
    this.snippet = snippet;
    return this;
  }

   /**
   * Get snippet
   * @return snippet
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public MembershipsLevelSnippet getSnippet() {
    return snippet;
  }


  public void setSnippet(MembershipsLevelSnippet snippet) {
    this.snippet = snippet;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MembershipsLevel membershipsLevel = (MembershipsLevel) o;
    return Objects.equals(this.etag, membershipsLevel.etag) &&
        Objects.equals(this.id, membershipsLevel.id) &&
        Objects.equals(this.kind, membershipsLevel.kind) &&
        Objects.equals(this.snippet, membershipsLevel.snippet);
  }

  @Override
  public int hashCode() {
    return Objects.hash(etag, id, kind, snippet);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MembershipsLevel {\n");
    sb.append("    etag: ").append(toIndentedString(etag)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    snippet: ").append(toIndentedString(snippet)).append("\n");
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


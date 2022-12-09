# HttpStreamFormat

Payload format for delivering to subscribers of HTTP streaming response bodies (`stream` hold mode). One of `content` or `content-bin` must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | A fragment of body data as a string. | [optional] 
**content_bin** | **str** | A fragment of body data as a base64-encoded binary blob. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



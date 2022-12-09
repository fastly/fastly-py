# HttpResponseFormat

Payload format for delivering to subscribers of whole HTTP responses (`response` hold mode). One of `body` or `body-bin` must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code. | [optional]  if omitted the server will use the default value of 200
**reason** | **str** | The HTTP status string. Defaults to a string appropriate for `code`. | [optional] 
**headers** | **{str: (str,)}** | A map of arbitrary HTTP response headers to include in the response. | [optional] 
**body** | **str** | The response body as a string. | [optional] 
**body_bin** | **str** | The response body as a base64-encoded binary blob. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



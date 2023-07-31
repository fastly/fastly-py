# ResponseObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_condition** | **str, none_type** | Name of the cache condition controlling when this configuration applies. | [optional] 
**content** | **str** | The content to deliver for the response object, can be empty. | [optional] 
**content_type** | **str, none_type** | The MIME type of the content, can be empty. | [optional] 
**name** | **str** | Name for the request settings. | [optional] 
**status** | **str** | The HTTP status code. | [optional]  if omitted the server will use the default value of "200"
**response** | **str** | The HTTP response. | [optional]  if omitted the server will use the default value of "Ok"
**request_condition** | **str, none_type** | Condition which, if met, will select this configuration during a request. Optional. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



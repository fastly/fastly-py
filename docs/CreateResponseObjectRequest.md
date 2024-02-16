# CreateResponseObjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the response object to create. | [optional] 
**status** | **str** | The status code the response will have. Defaults to 200. | [optional] 
**response** | **str** | The status text the response will have. Defaults to &#39;OK&#39;. | [optional] 
**content** | **str** | The content the response will deliver. | [optional] 
**content_type** | **str, none_type** | The MIME type of your response content. | [optional] 
**request_condition** | **str, none_type** | Condition which, if met, will select this configuration during a request. Optional. | [optional] 
**cache_condition** | **str, none_type** | Name of the cache condition controlling when this configuration applies. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Condition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**name** | **str** | Name of the condition. Required. | [optional] 
**priority** | **str** | A numeric string. Priority determines execution order. Lower numbers execute first. | [optional]  if omitted the server will use the default value of "100"
**statement** | **str** | A conditional expression in VCL used to determine if the condition is met. | [optional] 
**service_id** | **str** |  | [optional] [readonly] 
**version** | **str** | A numeric string that represents the service version. | [optional] 
**type** | **str** | Type of the condition. Required. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



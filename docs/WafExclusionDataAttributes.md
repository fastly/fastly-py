# WafExclusionDataAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | A conditional expression in VCL used to determine if the condition is met. | [optional] 
**exclusion_type** | **str** | The type of exclusion. | [optional] 
**logging** | **bool** | Whether to generate a log upon matching. | [optional]  if omitted the server will use the default value of True
**name** | **str** | Name of the exclusion. | [optional] 
**number** | **int** | A numeric ID identifying a WAF exclusion. | [optional] 
**variable** | **str, none_type** | The variable to exclude. An optional selector can be specified after the variable separated by a colon (`:`) to restrict the variable to a particular parameter. Required for `exclusion_type&#x3D;variable`. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Header


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Accepts a string value. | [optional] 
**cache_condition** | **str, none_type** | Name of the cache condition controlling when this configuration applies. | [optional] 
**dst** | **str** | Header to set. | [optional] 
**name** | **str** | A handle to refer to this Header object. | [optional] 
**regex** | **str, none_type** | Regular expression to use. Only applies to `regex` and `regex_repeat` actions. | [optional] 
**request_condition** | **str, none_type** | Condition which, if met, will select this configuration during a request. Optional. | [optional] 
**response_condition** | **str, none_type** | Optional name of a response condition to apply. | [optional] 
**src** | **str, none_type** | Variable to be used as a source for the header content. Does not apply to `delete` action. | [optional] 
**substitution** | **str, none_type** | Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions. | [optional] 
**type** | **str** | Accepts a string value. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



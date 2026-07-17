# PathChange

Modifications to an existing path between versions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_id** | **str** | Alphanumeric string identifying the path. Stable across versions of the routing config. | [optional] [readonly] 
**path** | **str** | The current path pattern. | [optional] 
**old_path** | **str** | The previous path pattern, if it changed. | [optional] 
**rules_added** | [**[RuleResponse]**](RuleResponse.md) | Rules that were added to this path. | [optional] 
**rules_changed** | [**[RuleChange]**](RuleChange.md) | Rules that were modified on this path. | [optional] 
**rules_deleted** | [**[RuleResponse]**](RuleResponse.md) | Rules that were removed from this path. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DraftDiff

The differences between the draft and active versions of a routing config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**[PathWithRules]**](PathWithRules.md) | Paths that exist in the draft but not in the active version. | [optional] 
**deleted** | [**[PathWithRules]**](PathWithRules.md) | Paths that exist in the active version but not in the draft. | [optional] 
**modified** | [**[PathChange]**](PathChange.md) | Paths that exist in both versions but have changed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



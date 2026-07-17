# RuleResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alphanumeric string identifying the rule. Stable across versions of the routing config. | [optional] [readonly] 
**is_default** | **bool** | Whether this is the default (catch-all) rule for the path. | [optional] [readonly] 
**action** | [**Action**](Action.md) |  | [optional] 
**conditions** | [**[RoutingConfigCondition]**](RoutingConfigCondition.md) | The conditions a request must satisfy for this rule to match. Empty for the default rule. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



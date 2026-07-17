# RuleCreate

All attributes for creating a rule. A rule with an empty `conditions` array is the default (catch-all) rule for its path.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**conditions** | [**[RoutingConfigCondition]**](RoutingConfigCondition.md) | The conditions a request must satisfy for this rule to match. An empty array indicates the default rule for the path. | 
**position** | [**Position**](Position.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



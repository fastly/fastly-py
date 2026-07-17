# RoutingConfigCondition

A condition that must be met for a rule to match.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConditionType**](ConditionType.md) |  | 
**operator** | [**ConditionOperator**](ConditionOperator.md) |  | 
**value** | **str** | The value to compare against using the operator. | 
**key** | **str** | The key to evaluate. For `header` conditions this is the header name. Required for `header` conditions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



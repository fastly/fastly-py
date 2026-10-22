# NetworkProtectNetwork

Shared Network Protect network attributes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NetworkProtectName**](NetworkProtectName.md) |  | 
**prefix** | **str** | The CIDR block to protect, masked to its network address. It cannot be changed after creation. | 
**endpoint_policies** | [**NetworkProtectNetworkEndpointPolicies**](NetworkProtectNetworkEndpointPolicies.md) |  | 
**advertise** | **bool** | Desired advertisement state, which is not the same as observed route state. Enabling it requires approved LOA, valid ROA, and a ready default-region delivery policy. A later ROA failure does not turn an existing advertisement off; losing LOA approval or the last ready default endpoint does. | defaults to False
**description** | [**NetworkProtectNetworkDescription**](NetworkProtectNetworkDescription.md) |  | [optional] 
**rule_set_id** | [**NetworkProtectNetworkRuleSetId**](NetworkProtectNetworkRuleSetId.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



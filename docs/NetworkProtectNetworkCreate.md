# NetworkProtectNetworkCreate

Attributes accepted when creating a network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NetworkProtectName**](NetworkProtectName.md) |  | 
**prefix** | **str** | The CIDR block to protect, masked to its network address. It cannot be changed after creation. | 
**description** | [**NetworkProtectNetworkDescription**](NetworkProtectNetworkDescription.md) |  | [optional] 
**rule_set_id** | [**NetworkProtectNetworkRuleSetIdCreate**](NetworkProtectNetworkRuleSetIdCreate.md) |  | [optional] 
**endpoint_policies** | [**NetworkProtectNetworkEndpointPolicies**](NetworkProtectNetworkEndpointPolicies.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



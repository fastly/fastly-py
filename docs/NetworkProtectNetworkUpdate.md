# NetworkProtectNetworkUpdate

Attributes accepted when updating a network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**NetworkProtectNetworkDescription**](NetworkProtectNetworkDescription.md) |  | [optional] 
**name** | [**NetworkProtectName**](NetworkProtectName.md) |  | [optional] 
**rule_set_id** | [**NetworkProtectNetworkRuleSetIdUpdate**](NetworkProtectNetworkRuleSetIdUpdate.md) |  | [optional] 
**endpoint_policies** | [**NetworkProtectNetworkEndpointPolicies**](NetworkProtectNetworkEndpointPolicies.md) |  | [optional] 
**advertise** | **bool** | Desired advertisement state, which is not the same as observed route state. Enabling it requires approved LOA, valid ROA, and a ready default-region delivery policy. A later ROA failure does not turn an existing advertisement off; losing LOA approval or the last ready default endpoint does. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



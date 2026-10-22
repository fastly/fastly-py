# NetworkProtectNetworkResponse

A Network Protect network response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NetworkProtectName**](NetworkProtectName.md) |  | 
**prefix** | **str** | The CIDR block to protect, masked to its network address. It cannot be changed after creation. | 
**endpoint_policies** | [**NetworkProtectNetworkEndpointPolicies**](NetworkProtectNetworkEndpointPolicies.md) |  | 
**id** | [**NetworkProtectResponseId**](NetworkProtectResponseId.md) |  | 
**created_at** | **datetime** | An ISO 8601 timestamp in UTC. | [readonly] 
**updated_at** | **datetime** | An ISO 8601 timestamp in UTC. | [readonly] 
**advertise** | **bool** | Desired advertisement state, which is not the same as observed route state. Enabling it requires approved LOA, valid ROA, and a ready default-region delivery policy. A later ROA failure does not turn an existing advertisement off; losing LOA approval or the last ready default endpoint does. | defaults to False
**description** | [**NetworkProtectNetworkDescription**](NetworkProtectNetworkDescription.md) |  | [optional] 
**rule_set_id** | [**NetworkProtectNetworkRuleSetId**](NetworkProtectNetworkRuleSetId.md) |  | [optional] 
**roa_status** | [**NetworkProtectRoaStatus**](NetworkProtectRoaStatus.md) |  | [optional] 
**roa_checked_at** | **datetime, none_type** | When Fastly last completed a ROA check. Null while the status is pending. A failed check leaves this unchanged; an old value can indicate delayed or failing checks. Null also means the controller did not report a check time. | [optional] [readonly] 
**roa_data_as_of** | **datetime, none_type** | When the RPKI dataset used by the last check was built. This is not the same as `roa_checked_at`; a recent check can use an older dataset. Null while the status is pending or when no dataset build time was reported. | [optional] [readonly] 
**loa_status** | [**NetworkProtectLoaStatus**](NetworkProtectLoaStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



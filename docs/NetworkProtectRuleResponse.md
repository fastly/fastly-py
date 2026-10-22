# NetworkProtectRuleResponse

A rule as returned by the API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_protocol** | [**NetworkProtectRuleIpProtocol**](NetworkProtectRuleIpProtocol.md) |  | 
**source_prefix_list_id** | [**NetworkProtectRuleSourcePrefixListId**](NetworkProtectRuleSourcePrefixListId.md) |  | 
**destination_ip_address** | **str** | Match traffic sent to this address; omit for any destination. An address outside a Network using this Rule Set never matches and still consumes one of the 64 rules. The API does not enforce containment in a network prefix; attached Rule Sets require a compatible IP family. | 
**source_ports** | [**NetworkProtectRuleSourcePorts**](NetworkProtectRuleSourcePorts.md) |  | 
**destination_ports** | [**NetworkProtectRuleDestinationPorts**](NetworkProtectRuleDestinationPorts.md) |  | 
**created_at** | **datetime** | An ISO 8601 timestamp in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | An ISO 8601 timestamp in UTC. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



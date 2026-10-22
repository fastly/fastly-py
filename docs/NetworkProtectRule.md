# NetworkProtectRule

One ordered firewall rule. All match fields are optional, but at least one must be provided. The action is required. Rules have no public ID; replacing the list preserves timestamps only when logical fields, comment, and position are unchanged.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**NetworkProtectRuleAction**](NetworkProtectRuleAction.md) |  | 
**ip_protocol** | [**NetworkProtectRuleIpProtocol**](NetworkProtectRuleIpProtocol.md) |  | 
**source_prefix_list_id** | [**NetworkProtectRuleSourcePrefixListId**](NetworkProtectRuleSourcePrefixListId.md) |  | 
**destination_ip_address** | **str** | Match traffic sent to this address; omit for any destination. An address outside a Network using this Rule Set never matches and still consumes one of the 64 rules. The API does not enforce containment in a network prefix; attached Rule Sets require a compatible IP family. | 
**source_ports** | [**NetworkProtectRuleSourcePorts**](NetworkProtectRuleSourcePorts.md) |  | 
**destination_ports** | [**NetworkProtectRuleDestinationPorts**](NetworkProtectRuleDestinationPorts.md) |  | 
**comment** | [**NetworkProtectRuleComment**](NetworkProtectRuleComment.md) |  | [optional] 
**ip_protocol** | [**NetworkProtectRuleIpProtocol**](NetworkProtectRuleIpProtocol.md) |  | [optional] 
**source_prefix_list_id** | [**NetworkProtectRuleSourcePrefixListId**](NetworkProtectRuleSourcePrefixListId.md) |  | [optional] 
**destination_ip_address** | **str** | Match traffic sent to this address; omit for any destination. An address outside a Network using this Rule Set never matches and still consumes one of the 64 rules. The API does not enforce containment in a network prefix; attached Rule Sets require a compatible IP family. | [optional] 
**source_ports** | [**NetworkProtectRuleSourcePorts**](NetworkProtectRuleSourcePorts.md) |  | [optional] 
**destination_ports** | [**NetworkProtectRuleDestinationPorts**](NetworkProtectRuleDestinationPorts.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ComputeAclUpdateEntry

Defines the structure of an ACL update request entry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | One of \&quot;create\&quot;, \&quot;update\&quot;, or \&quot;delete\&quot; indicating the operation to perform on the update. | [optional] 
**prefix** | **str** | An IP prefix defined in Classless Inter-Domain Routing (CIDR) format, i.e. a valid IP address (v4 or v6) followed by a forward slash (/) and a prefix length (0-32 or 0-128, depending on address family). | [optional] 
**action** | **str** | The action taken on the IP address, one of \&quot;BLOCK\&quot; or \&quot;ALLOW\&quot;. If using the \&quot;delete\&quot; operation, no action should be specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



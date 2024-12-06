# ComputeAclUpdateEntry

Defines the structure of an ACL update request entry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | One of \&quot;create\&quot; or \&quot;update\&quot;, indicating that the rest of this entry is to be added to/updated in the ACL. | [optional] 
**prefix** | **str** | An IP prefix defined in Classless Inter-Domain Routing (CIDR) format, i.e. a valid IP address (v4 or v6) followed by a forward slash (/) and a prefix length (0-32 or 0-128, depending on address family). | [optional] 
**action** | **str** | The action taken on the IP address, either \&quot;block\&quot; or \&quot;allow\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



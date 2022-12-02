# AclEntryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negated** | **int** | Whether to negate the match. Useful primarily when creating individual exceptions to larger subnets. | [optional]  if omitted the server will use the default value of 0
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**ip** | **str** | An IP address. | [optional] 
**subnet** | **int, none_type** | Number of bits for the subnet mask applied to the IP address. For IPv4 addresses, a value of 32 represents the smallest subnet mask (1 address), 24 represents a class C subnet mask (256 addresses), 16 represents a class B subnet mask (65k addresses), and 8 is class A subnet mask (16m addresses). If not provided, no mask is applied. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**acl_id** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**service_id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IamV1RoleListResponse

Paginated list of IAM roles.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results returned. | [optional] 
**next_cursor** | **str** | Cursor for the next page. | [optional] 
**data** | [**[IamV1RoleResponse]**](IamV1RoleResponse.md) | Page of IAM roles (length ≤ limit). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NetworkProtectConflict

Conflict returned when resource state prevents the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Short summary of the conflict. | 
**detail** | **str** | Explanation of the conflicting resource state. | 
**status** | **int** | HTTP status code for this error. | defaults to 409
**errors** | [**NetworkProtectConflictErrors**](NetworkProtectConflictErrors.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



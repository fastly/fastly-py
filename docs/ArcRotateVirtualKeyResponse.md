# ArcRotateVirtualKeyResponse

The virtual key that was rotated, including its new access token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the virtual key. | [readonly] 
**customer_id** | **str** | The ID of the customer account that owns the key. | [readonly] 
**name** | **str** | The display name of the virtual key. | 
**user_id** | **str** | The ID of the user who created the key. | [readonly] 
**created_at** | **datetime** | The date and time the key was created, in RFC 3339 format. | [readonly] 
**updated_at** | **datetime** | The date and time the key was last updated, in RFC 3339 format. | [readonly] 
**access_token** | **str** | The new access token for this virtual key. This is only returned when the key is created or rotated, and cannot be retrieved again afterward. | [readonly] 
**expires_at** | **datetime, none_type** | The date and time the key expires, in RFC 3339 format. `null` if the key doesn&#39;t expire. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



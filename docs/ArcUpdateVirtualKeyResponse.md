# ArcUpdateVirtualKeyResponse

The virtual key after the update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the virtual key. | [readonly] 
**customer_id** | **str** | The ID of the customer account that owns the key. | [readonly] 
**name** | **str** | The display name of the virtual key. | 
**user_id** | **str** | The ID of the user who created the key. | [readonly] 
**created_at** | **datetime** | The date and time the key was created, in RFC 3339 format. | [readonly] 
**updated_at** | **datetime** | The date and time the key was last updated, in RFC 3339 format. | [readonly] 
**expires_at** | **datetime, none_type** | The date and time the key expires, in RFC 3339 format. `null` if the key doesn&#39;t expire. | [optional] 
**rpm_limit** | **int, none_type** | The requests-per-minute limit for this key. `null` if there is no limit. | [optional] 
**tpm_limit** | **int, none_type** | The tokens-per-minute limit for this key. `null` if there is no limit. | [optional] 
**spend_limit_enabled** | **bool** | Whether a spend limit is enabled for this key. | [optional] [readonly] 
**spend_limit_enabled_on** | **datetime, none_type** | The date and time `spend_limit_enabled` was last set to `true`, in RFC 3339 format. `null` if the spend limit has never been enabled. This timestamp is not cleared when `spend_limit_enabled` is later set back to `false`, so it can be non-null even when the spend limit is currently disabled.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



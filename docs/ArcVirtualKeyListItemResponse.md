# ArcVirtualKeyListItemResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the virtual key. | 
**id** | **str** | The unique identifier of the virtual key. | [readonly] 
**customer_id** | **str** | The ID of the customer account that owns the key. | [readonly] 
**type** | **str** | The type of the resource. | [readonly] 
**user_id** | **str** | The ID of the user who created the key. | [readonly] 
**created_at** | **datetime** | The date and time the key was created, in RFC 3339 format. | [readonly] 
**updated_at** | **datetime** | The date and time the key was last updated, in RFC 3339 format. | [readonly] 
**expires_at** | **datetime, none_type** | The date and time the key expires, in RFC 3339 format. Omit for a key that doesn&#39;t expire. | [optional] 
**security_enabled** | **bool** | Whether AI Firewall security is enabled for requests made with this key. | [optional]  if omitted the server will use the default value of False
**security_action** | **str** | The action AI Firewall takes when it detects a violation on a request made with this key. Only meaningful when `security_enabled` is `true`. | [optional] 
**rpm_limit** | **int, none_type** | The requests-per-minute limit for this key. Omit for no limit. | [optional] 
**tpm_limit** | **int, none_type** | The tokens-per-minute limit for this key. Omit for no limit. | [optional] 
**user_name** | **str** | The display name of the user who created the key. | [optional] [readonly] 
**last_used_at** | **datetime, none_type** | The date and time the key was last used to make a request, in RFC 3339 format. `null` if the key has never been used. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | The date and time the key was deleted, in RFC 3339 format. `null` unless the key was deleted and `include_deleted` was used to retrieve it. | [optional] [readonly] 
**spend_limit_enabled** | **bool** | Whether a spend limit is enabled for this key. | [optional] [readonly] 
**spend_limit_enabled_on** | **datetime, none_type** | The date and time `spend_limit_enabled` was last set to `true`, in RFC 3339 format. `null` if the spend limit has never been enabled. This timestamp is not cleared when `spend_limit_enabled` is later set back to `false`, so it can be non-null even when the spend limit is currently disabled.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



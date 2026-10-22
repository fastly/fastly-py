# ArcUpdateVirtualKeyRequest

A partial update to a virtual key. Only the fields you include are changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the virtual key. | [optional] 
**expires_at** | **datetime, none_type** | The date and time the key expires, in RFC 3339 format. Set explicitly to `null` to clear the expiration.  | [optional] 
**security_enabled** | **bool** | Whether AI Firewall security is enabled for requests made with this key. | [optional] 
**security_action** | **str** | The action AI Firewall takes when it detects a violation on a request made with this key. | [optional] 
**rpm_limit** | **int, none_type** | The requests-per-minute limit for this key. Omit this field to leave the limit unchanged, set it to a positive integer to set a limit, or set it explicitly to `null` to remove the limit.  | [optional] 
**tpm_limit** | **int, none_type** | The tokens-per-minute limit for this key. Omit this field to leave the limit unchanged, set it to a positive integer to set a limit, or set it explicitly to `null` to remove the limit.  | [optional] 
**spend_limit_enabled** | **bool** | Whether a spend limit is enabled for this key. This field cannot be set when the key is created; it can only be changed with this endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



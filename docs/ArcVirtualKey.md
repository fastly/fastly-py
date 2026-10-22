# ArcVirtualKey

A virtual key used to authenticate requests through the AI Runtime Control gateway.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the virtual key. | 
**expires_at** | **datetime, none_type** | The date and time the key expires, in RFC 3339 format. Omit for a key that doesn&#39;t expire. | [optional] 
**security_enabled** | **bool** | Whether AI Firewall security is enabled for requests made with this key. | [optional]  if omitted the server will use the default value of False
**security_action** | **str** | The action AI Firewall takes when it detects a violation on a request made with this key. Only meaningful when `security_enabled` is `true`. | [optional] 
**rpm_limit** | **int, none_type** | The requests-per-minute limit for this key. Omit for no limit. | [optional] 
**tpm_limit** | **int, none_type** | The tokens-per-minute limit for this key. Omit for no limit. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



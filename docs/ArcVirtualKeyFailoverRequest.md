# ArcVirtualKeyFailoverRequest

A failover policy for a virtual key. `targets` are tried in order after the primary request fails and one of the enabled error conditions is met. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**[ArcFailoverTarget]**](ArcFailoverTarget.md) | The provider connections to retry against, in order. | 
**timeout_enabled** | **bool** | Whether a request timeout triggers failover. | [optional] 
**rate_limit_429_enabled** | **bool** | Whether a `429 Too Many Requests` response from the provider triggers failover. | [optional] 
**server_error_5xx_enabled** | **bool** | Whether a `5xx` server error response from the provider triggers failover. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



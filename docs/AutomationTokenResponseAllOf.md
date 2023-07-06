# AutomationTokenResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ReadOnlyId**](ReadOnlyId.md) |  | [optional] 
**customer_id** | [**ReadOnlyCustomerId**](ReadOnlyCustomerId.md) |  | [optional] 
**role** | **str** |  | [optional] 
**ip** | **str** | The IP address of the client that last used the token. | [optional] 
**user_agent** | **str** | The User-Agent header of the client that last used the token. | [optional] 
**sudo_expires_at** | **str** |  | [optional] [readonly] 
**last_used_at** | **datetime** | A UTC time-stamp of when the token was last used. | [optional] [readonly] 
**created_at** | **str** | A UTC time-stamp of when the token was created. | [optional] 
**expires_at** | **str** | (optional) A UTC time-stamp of when the token will expire. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AutomationTokenCreateResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ReadOnlyId**](ReadOnlyId.md) |  | [optional] 
**user_id** | [**ReadOnlyUserId**](ReadOnlyUserId.md) |  | [optional] 
**customer_id** | [**ReadOnlyCustomerId**](ReadOnlyCustomerId.md) |  | [optional] 
**created_at** | **datetime** | A UTC timestamp of when the token was created.  | [optional] [readonly] 
**access_token** | **str** |  | [optional] [readonly] 
**tls_access** | **bool** | Indicates whether TLS access is enabled for the token. | [optional] 
**last_used_at** | **datetime** | A UTC timestamp of when the token was last used. | [optional] [readonly] 
**user_agent** | **str** | The User-Agent header of the client that last used the token. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



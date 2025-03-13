# AutomationTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the token. | [optional] 
**role** | **str** |  | [optional] 
**services** | **[str]** | (Optional) The service IDs of the services the token will have access to. Separate service IDs with a space. If no services are specified, the token will have access to all services on the account.  | [optional] 
**scope** | **str** | A space-delimited list of authorization scope. | [optional]  if omitted the server will use the default value of "global"
**expires_at** | **str** | (optional) A UTC timestamp of when the token will expire. | [optional] 
**id** | [**ReadOnlyId**](ReadOnlyId.md) |  | [optional] 
**customer_id** | [**ReadOnlyCustomerId**](ReadOnlyCustomerId.md) |  | [optional] 
**ip** | **str** | The IP address of the client that last used the token. | [optional] 
**user_agent** | **str** | The User-Agent header of the client that last used the token. | [optional] 
**tls_access** | **bool** | Indicates whether TLS access is enabled for the token. | [optional] 
**last_used_at** | **datetime** | A UTC timestamp of when the token was last used. | [optional] [readonly] 
**created_at** | **str** | A UTC timestamp of when the token was created. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



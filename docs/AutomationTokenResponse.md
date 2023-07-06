# AutomationTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the token. | [optional] 
**role** | **str** |  | [optional] 
**services** | **[str]** | (Optional) The service IDs of the services the token will have access to. Separate service IDs with a space. If no services are specified, the token will have access to all services on the account.  | [optional] 
**scope** | **str** | A space-delimited list of authorization scope. | [optional]  if omitted the server will use the default value of "global"
**expires_at** | **str** | (optional) A UTC time-stamp of when the token will expire. | [optional] 
**created_at** | **str** | A UTC time-stamp of when the token was created. | [optional] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | [**ReadOnlyId**](ReadOnlyId.md) |  | [optional] 
**customer_id** | [**ReadOnlyCustomerId**](ReadOnlyCustomerId.md) |  | [optional] 
**ip** | **str** | The IP address of the client that last used the token. | [optional] 
**user_agent** | **str** | The User-Agent header of the client that last used the token. | [optional] 
**sudo_expires_at** | **str** |  | [optional] [readonly] 
**last_used_at** | **datetime** | A UTC time-stamp of when the token was last used. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



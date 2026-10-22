# AutomationTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the token. | [optional] 
**role** | **str** |  | [optional] 
**roles** | [**[AutomationTokenRole]**](AutomationTokenRole.md) | All roles assigned to the token. Each role includes an `id` and `name`. | [optional] 
**services** | **[str]** | The service IDs of the services the token has access to. Empty when `limit_services` is `false` (full access) or when the token has no service access. | [optional] 
**limit_services** | **bool** | When `true`, the token is restricted to only the services in the `services` array. When `false`, the token has access to all services. | [optional] 
**limit_workspaces** | **bool** | When `true`, the token is restricted to only the workspaces in the `workspaces` array. When `false`, the token has access to all workspaces. Only applies to roles that support workspace access. | [optional] 
**workspaces** | **[str]** | The workspace IDs of the workspaces the token has access to. Returns an empty array for tokens without workspace access. | [optional] 
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



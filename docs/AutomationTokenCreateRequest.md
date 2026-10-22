# AutomationTokenCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the token. | 
**expires_at** | **datetime, none_type** | A UTC timestamp of when the token will expire. | 
**role** | **str** | The role for the token. The `roles` field is the preferred way to assign roles. This field is supported for backwards compatibility with single-role tokens. | [optional] 
**roles** | **[str]** | Array of role IDs to assign to the token. Use this field for tokens with multiple roles. When provided, this takes precedence over the `role` field. To get available role IDs, use [GET /roles](https://www.fastly.com/documentation/reference/api/account/roles/). | [optional] 
**services** | **[str]** | List of service IDs the token can access. Only used when `limit_services` is `true`. | [optional] 
**limit_services** | **bool** | When `true`, restricts the token to only the services specified in the `services` array. When `false` (default), the token has access to all services. | [optional]  if omitted the server will use the default value of False
**limit_workspaces** | **bool** | When `true` (default), restricts the token to only the workspaces specified in the `workspaces` array. When `false`, the token has access to all workspaces. Only applies to roles that support workspace access (such as Next-Gen WAF roles). For roles without workspace support, this field has no effect. | [optional]  if omitted the server will use the default value of True
**workspaces** | **[str]** | List of workspace IDs the token can access. Only used when `limit_workspaces` is `true` and the token has roles that support workspace access. | [optional] 
**scope** | **str** |  | [optional]  if omitted the server will use the default value of "global"
**tls_access** | **bool** | Indicates whether TLS access is enabled for the token. Only applicable when using the single-role `role` field. For tokens with multiple roles, assign TLS roles (`tls_admin` or `tls_viewer`) via the `roles` field instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



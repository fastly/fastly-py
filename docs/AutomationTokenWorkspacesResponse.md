# AutomationTokenWorkspacesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[AutomationTokenWorkspace]**](AutomationTokenWorkspace.md) | Workspaces the token can access. Empty if the token has no workspace-specific permissions or if `limit_workspaces` is `false` (unrestricted access). | 
**meta** | [**AutomationTokenWorkspacesMeta**](AutomationTokenWorkspacesMeta.md) |  | 
**limit_workspaces** | **bool** | Indicates whether workspace access is restricted: - `true`: Token can only access workspaces listed in `data` - `false`: Token has unrestricted access to all workspaces  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



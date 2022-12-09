# TokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | **[str]** | List of alphanumeric strings identifying services (optional). If no services are specified, the token will have access to all services on the account.  | [optional] [readonly] 
**name** | **str** | Name of the token. | [optional] 
**scope** | **str** | Space-delimited list of authorization scope. | [optional]  if omitted the server will use the default value of "global"
**created_at** | **str** | Time-stamp (UTC) of when the token was created. | [optional] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**user_id** | **str** |  | [optional] [readonly] 
**last_used_at** | **str** | Time-stamp (UTC) of when the token was last used. | [optional] [readonly] 
**expires_at** | **str** | Time-stamp (UTC) of when the token will expire (optional). | [optional] 
**ip** | **str** | IP Address of the client that last used the token. | [optional] 
**user_agent** | **str** | User-Agent header of the client that last used the token. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



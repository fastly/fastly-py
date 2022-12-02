# Token


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | **[str]** | List of alphanumeric strings identifying services (optional). If no services are specified, the token will have access to all services on the account.  | [optional] [readonly] 
**name** | **str** | Name of the token. | [optional] 
**scope** | **str** | Space-delimited list of authorization scope. | [optional]  if omitted the server will use the default value of "global"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



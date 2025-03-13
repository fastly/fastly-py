# AutomationTokenCreateRequestAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the token | [optional] 
**role** | **str** |  | [optional] 
**services** | **[str]** | List of service ids to limit the token | [optional] 
**scope** | **str** |  | [optional]  if omitted the server will use the default value of "global"
**expires_at** | **datetime, none_type** | A UTC timestamp of when the token will expire. | [optional] 
**tls_access** | **bool** | Indicates whether TLS access is enabled for the token. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



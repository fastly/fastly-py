# VersionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether this is the active version or not. | [optional]  if omitted the server will use the default value of False
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**deployed** | **bool** | Unused at this time. | [optional] 
**locked** | **bool** | Whether this version is locked or not. Objects can not be added or edited on locked versions. | [optional]  if omitted the server will use the default value of False
**number** | **int** | The number of this version. | [optional] [readonly] 
**staging** | **bool** | Unused at this time. | [optional]  if omitted the server will use the default value of False
**testing** | **bool** | Unused at this time. | [optional]  if omitted the server will use the default value of False
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**service_id** | **str** |  | [optional] [readonly] 
**environments** | [**[Environment]**](Environment.md) | A list of environments where the service has been deployed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



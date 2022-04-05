# SchemasSnippetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the snippet. | [optional] 
**dynamic** | **int** | Sets the snippet version. | [optional] 
**type** | **str** | The location in generated VCL where the snippet should be placed. | [optional] 
**content** | **str** | The VCL code that specifies exactly what the snippet does. | [optional] 
**priority** | **int** | Priority determines execution order. Lower numbers execute first. | [optional]  if omitted the server will use the default value of 100
**service_id** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**version** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


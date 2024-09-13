# ServiceDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**name** | **str** | The name of the service. | [optional] 
**customer_id** | **str** | Alphanumeric string identifying the customer. | [optional] 
**type** | **str** | The type of this service. | [optional] 
**id** | **str** |  | [optional] [readonly] 
**publish_key** | **str** | Unused at this time. | [optional] 
**paused** | **bool** | Whether the service is paused. Services are paused due to a lack of traffic for an extended period of time. Services are resumed either when a draft version is activated or a locked version is cloned and reactivated. | [optional] 
**versions** | [**[SchemasVersionResponse]**](SchemasVersionResponse.md) | A list of [versions](https://www.fastly.com/documentation/reference/api/services/version/) associated with the service. | [optional] 
**environments** | [**[Environment]**](Environment.md) | A list of environments where the service has been deployed. | [optional] 
**active_version** | [**ServiceVersionDetailOrNull**](ServiceVersionDetailOrNull.md) |  | [optional] 
**version** | [**ServiceVersionDetail**](ServiceVersionDetail.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



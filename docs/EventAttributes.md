# EventAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** | Indicates if event was performed by Fastly. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**customer_id** | **str** |  | [optional] [readonly] 
**description** | **str** | Description of the event. | [optional] 
**event_type** | **str** | Type of event. Can be used with `filter[event_type]` | [optional] 
**ip** | **str** | IP addresses that the event was requested from. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Hash of key value pairs of additional information. | [optional] 
**service_id** | **str** |  | [optional] [readonly] 
**user_id** | **str** |  | [optional] [readonly] 
**token_id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



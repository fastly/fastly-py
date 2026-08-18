# LogError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_number** | **int** | Sequence number for ordering messages. | [optional] 
**error_time_us** | **int** | Timestamp of the error in microseconds. | [optional] 
**stream** | **str** | The stream type, always &#39;logging_error&#39; for logging endpoint errors. | [optional] 
**message** | **str** | User-friendly error message. | [optional] 
**endpoint** | **str** | Name of the logging endpoint that generated the error. | [optional] 
**details** | **str** | Additional error details as a JSON string. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



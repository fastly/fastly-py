# BotRequestMetricsMetadata

Meta information about the scope of the current response and optional additional information for subsequent requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **datetime** | An RFC-8339-formatted date and time string indicating the inclusive start of the query time range. | [optional] 
**to** | **datetime** | An RFC-8339-formatted date and time indicating the exclusive end of the query time range. | [optional] 
**group_by** | **str** | List of dimensions (comma-separated) being summed over in the results. | [optional] 
**next_cursor** | **str** | Optional string that can be used to request the next page of results, if any. | [optional] 
**limit** | **int** | The maximum number of results to return. Defaults to 1000. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OriginInspectorHistoricalMeta

Meta information about the scope of the query in a human readable format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start time that was used to perform the query as an ISO-8601-formatted date and time. | [optional] 
**end** | **str** | End time that was used to perform the query as an ISO-8601-formatted date and time. | [optional] 
**downsample** | **str** | Downsample that was used to perform the query. One of `minute`, `hour` or `day`. | [optional] 
**metrics** | **str** | A comma-separated list of the metrics that were requested. | [optional] 
**limit** | **float** | The maximum number of results shown per page. | [optional] 
**next_cursor** | **str** | A string that can be used to request the next page of results, if any. | [optional] 
**sort** | **str** | A comma-separated list of keys the results are sorted by. | [optional] 
**group_by** | **str** | A comma-separated list of dimensions being summed over in the query. | [optional] 
**filters** | [**OriginInspectorHistoricalMetaFilters**](OriginInspectorHistoricalMetaFilters.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginationMeta

Cursor-based pagination metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of records returned per page. | [optional] 
**next_cursor** | **str** | Cursor value used to retrieve the next page of results. Empty if there are no more results. | [optional] 
**previous_cursor** | **str** | Cursor value used to retrieve the previous page of results. Empty if there is no previous page. | [optional] 
**sort** | **str** | The sort order applied to the results. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Metadata

Pagination metadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | The token used to request the next set of results. | [optional] 
**limit** | **int** | The number of invoices included in the response. | [optional] 
**sort** | **str** | The sort order of the invoices in the response. | [optional]  if omitted the server will use the default value of "billing_start_date"
**total** | **int** | Total number of records available on the backend. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetLogRecordsResponseMetaFilters

Echoes the filters that were supplied in the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Specifies the ID of the service for which data should be returned. | [optional] 
**start** | **str** | Start time for the query as supplied in the request. | [optional] 
**end** | **str** | End time for the query as supplied in the request. | [optional] 
**domain_exact_match** | **bool** | Value of the `domain_exact_match` filter as supplied in the request. | [optional] 
**limit** | [**MetaPerPage**](MetaPerPage.md) |  | [optional] 
**next_cursor** | **str, none_type** | A cursor to specify the next page of results, if any. | [optional] 
**filter_fields** | [**[FilterFieldItem], none_type**](FilterFieldItem.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



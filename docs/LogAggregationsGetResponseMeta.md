# LogAggregationsGetResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Specifies the ID of the service for which data should be returned. | [optional] 
**start** | **str** | Start time for the query as supplied in the request. | [optional] 
**end** | **str** | End time for the query as supplied in the request. | [optional] 
**limit** | [**MetaPerPage**](MetaPerPage.md) |  | [optional] 
**sort** | **str** | Comma-separated list of the series names whose values were used to sort the results. | [optional] 
**filters** | [**LogAggregationsGetResponseMetaFilters**](LogAggregationsGetResponseMetaFilters.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



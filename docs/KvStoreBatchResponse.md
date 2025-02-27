# KvStoreBatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A descriptor for the response of the entire batch | [optional] 
**type** | **str** | If an error is present in any of the requests, this field will describe that error | [optional] 
**errors** | [**[KvStoreBatchResponseErrors]**](KvStoreBatchResponseErrors.md) | Errors which occurred while handling the items in the request | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



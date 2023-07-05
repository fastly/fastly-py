# Batch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A descriptor for the response of the entire batch | [optional] 
**type** | **str** | If an error is present in any of the requests, this field will describe that error | [optional] 
**errors** | [**[BatchErrors]**](BatchErrors.md) | Per-key errors which failed to parse, validate, or otherwise transmit | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



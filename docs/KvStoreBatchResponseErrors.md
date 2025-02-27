# KvStoreBatchResponseErrors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that the error corresponds to. This field will be empty if the object or one of its fields was not parseable. | [optional] 
**index** | **int** | The line number of the batch request body on which the error occurred (starting from 0 for the first line). | [optional] 
**code** | **str** | The HTTP response code for the item, or a 400 if the item&#39;s operation was not completed. | [optional] 
**reason** | **str** | A descriptor of this particular item&#39;s error. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



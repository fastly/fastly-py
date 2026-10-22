# NetworkProtectInvalidRequest

Validation error returned for an invalid request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Short summary of the validation problem. | 
**detail** | **str** | Corrective explanation for the invalid request. | 
**errors** | [**NetworkProtectErrorDetails**](NetworkProtectErrorDetails.md) |  | 
**status** | **int** | HTTP status code for this error. | defaults to 400
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



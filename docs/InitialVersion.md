# InitialVersion

Optional initial version payload to seed the new routing config with paths and rules in a single request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **bool** | Whether to activate the initial version on creation. | [optional]  if omitted the server will use the default value of False
**comment** | **str** | A freeform comment for the initial version. | [optional] 
**paths** | [**[InitialVersionPath]**](InitialVersionPath.md) | The paths to create on the initial version. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApexRedirect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**status_code** | **int** | HTTP status code used to redirect the client. | [optional] 
**domains** | **[str]** | Array of apex domains that should redirect to their WWW subdomain. | [optional] 
**feature_revision** | **int** | Revision number of the apex redirect feature implementation. Defaults to the most recent revision. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



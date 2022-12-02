# SettingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_default_host** | **str** | The default host name for the version. | [optional] 
**general_default_ttl** | **int** | The default time-to-live (TTL) for the version. | [optional] 
**general_stale_if_error** | **bool** | Enables serving a stale object if there is an error. | [optional]  if omitted the server will use the default value of False
**general_stale_if_error_ttl** | **int** | The default time-to-live (TTL) for serving the stale object for the version. | [optional]  if omitted the server will use the default value of 43200
**service_id** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



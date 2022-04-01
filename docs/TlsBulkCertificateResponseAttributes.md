# TlsBulkCertificateResponseAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**not_after** | **datetime** | Time-stamp (GMT) when the certificate will expire. Must be in the future to be used to terminate TLS traffic. | [optional] [readonly] 
**not_before** | **datetime** | Time-stamp (GMT) when the certificate will become valid. Must be in the past to be used to terminate TLS traffic. | [optional] [readonly] 
**replace** | **bool** | A recommendation from Fastly indicating the key associated with this certificate is in need of rotation. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



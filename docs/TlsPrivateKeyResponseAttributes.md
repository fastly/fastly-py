# TlsPrivateKeyResponseAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**name** | **str** | A customizable name for your private key. | [optional] 
**key_length** | **int** | The key length used to generate the private key. | [optional] [readonly] 
**key_type** | **str** | The algorithm used to generate the private key. Must be `RSA`. | [optional] [readonly] 
**replace** | **bool** | A recommendation from Fastly to replace this private key and all associated certificates. | [optional] [readonly] 
**public_key_sha1** | **str** | Useful for safely identifying the key. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



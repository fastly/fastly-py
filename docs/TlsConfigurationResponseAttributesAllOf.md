# TlsConfigurationResponseAttributesAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Signifies whether or not Fastly will use this configuration as a default when creating a new [TLS Activation](https://www.fastly.com/documentation/reference/api/tls/custom-certs/activations/). | [optional] [readonly] 
**http_protocols** | **[str]** | HTTP protocols available on your configuration. | [optional] [readonly] 
**tls_protocols** | **[str]** | TLS protocols available on your configuration. | [optional] [readonly] 
**bulk** | **bool** | Signifies whether the configuration is used for Platform TLS or not. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



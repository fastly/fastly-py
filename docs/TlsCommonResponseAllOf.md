# TlsCommonResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls_ca_cert** | **str, none_type** | A secure certificate to authenticate a server with. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_client_cert** | **str, none_type** | The client certificate used to make authenticated requests. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_client_key** | **str, none_type** | The client private key used to make authenticated requests. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_cert_hostname** | **str, none_type** | The hostname used to verify a server&#39;s certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN). | [optional]  if omitted the server will use the default value of "null"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



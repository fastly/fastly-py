# MutualAuthenticationDataAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_bundle** | **str** | One or more certificates. Enter each individual certificate blob on a new line. Must be PEM-formatted. Required on create. You may optionally rotate the cert_bundle on update. | [optional] 
**enforced** | **bool** | Determines whether Mutual TLS will fail closed (enforced) or fail open. A true value will require a successful Mutual TLS handshake for the connection to continue and will fail closed if unsuccessful. A false value will fail open and allow the connection to proceed. Optional. Defaults to true. | [optional] 
**name** | **str** | A custom name for your mutual authentication. Optional. If name is not supplied we will auto-generate one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



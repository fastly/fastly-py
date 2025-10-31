# SuccessfulResponseAsObjectAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain Identifier (UUID). | [optional] 
**fqdn** | **str** | The fully-qualified domain name for your domain. Can be created, but not updated. | [optional] 
**service_id** | **str, none_type** | The `service_id` associated with your domain or `null` if there is no association. | [optional] 
**description** | **str** | A freeform descriptive note. | [optional] 
**activated** | **bool** | Denotes if the domain has at least one TLS activation or not. | [optional] [readonly] 
**verified** | **bool** | Denotes that the customer has proven ownership over the domain by obtaining a Fastly-managed TLS certificate for it or by providing a their own TLS certificate from a publicly-trusted CA that includes the domain or matching wildcard.      | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



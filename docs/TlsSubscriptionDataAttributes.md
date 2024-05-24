# TlsSubscriptionDataAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_authority** | **str** | The entity that issues and certifies the TLS certificates for your subscription, either `certainly`, `lets-encrypt`, or `globalsign`. To migrate the subscription from one certificate authority to another, such as to migrate from &#39;lets-encrypt&#39; to &#39;certainly&#39;,  pass `certificate_authority` to the PATCH endpoint. To migrate from &#39;globalsign&#39; to &#39;certainly&#39;, contact Fastly Support. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



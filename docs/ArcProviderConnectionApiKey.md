# ArcProviderConnectionApiKey

A provider connection authenticated with the provider's own API key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the provider connection. Cannot match a name reserved by a built-in provider. | 
**models** | **[str]** | The AI model identifiers this connection is allowed to use. | 
**base_url** | **str** | The base URL of the provider&#39;s API. Must be an absolute `http` or `https` URL and must not end in `/v1`. | 
**api_key** | **str** | The provider&#39;s secret API key. | 
**auth_type** | **str** | The authentication type for this connection. Omit for the default `api-key` behavior. | [optional]  if omitted the server will use the default value of "api-key"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



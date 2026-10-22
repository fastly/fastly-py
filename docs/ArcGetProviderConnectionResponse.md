# ArcGetProviderConnectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the provider connection. | [readonly] 
**secret_id** | **str** | An opaque identifier for the secret material backing this connection. Not the secret itself. | [readonly] 
**name** | **str** | The display name of the provider connection. | 
**models** | **[str]** | The AI model identifiers this connection is allowed to use. | 
**auth_type** | **str** | The authentication type for this connection. | 
**created_at** | **datetime** | The date and time the connection was created, in RFC 3339 format. | [readonly] 
**updated_at** | **datetime** | The date and time the connection was last updated, in RFC 3339 format. | [readonly] 
**virtual_key_ids** | **[str]** | The IDs of the active virtual keys whose failover policy references this connection. Empty if no virtual key references it. | [readonly] 
**base_url** | **str** | The base URL of the provider&#39;s API. Present only for `api-key` connections. | [optional] 
**region** | **str** | The AWS region for Bedrock API requests. Present only for `aws-iam` connections. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



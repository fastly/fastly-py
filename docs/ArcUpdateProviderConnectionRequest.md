# ArcUpdateProviderConnectionRequest

A partial update to a provider connection. Only the fields you include are changed. `models`, `base_url`, and `api_key` apply to `api-key` connections; `customer_role_arn` and `region` apply to `aws-iam` connections. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **[str]** | The AI model identifiers this connection is allowed to use. Must be non-empty if included. | [optional] 
**base_url** | **str** | The base URL of the provider&#39;s API (`api-key` connections only). | [optional] 
**api_key** | **str** | The provider&#39;s secret API key (`api-key` connections only). | [optional] 
**customer_role_arn** | **str** | The ARN of the IAM role to assume for Bedrock requests (`aws-iam` connections only). | [optional] 
**region** | **str** | The AWS region for Bedrock API requests (`aws-iam` connections only). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



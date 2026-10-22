# ArcProviderConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The provider name. Must be `bedrock` for `aws-iam` connections. | [optional]  if omitted the server will use the default value of "bedrock"
**models** | **[str]** | The Bedrock model identifiers this connection is allowed to use. | [optional] 
**base_url** | **str** | The base URL of the provider&#39;s API. Must be an absolute `http` or `https` URL and must not end in `/v1`. | [optional] 
**api_key** | **str** | The provider&#39;s secret API key. | [optional] 
**auth_type** | **str** | The authentication type for this connection. | [optional]  if omitted the server will use the default value of "aws-iam"
**customer_role_arn** | **str** | The ARN of the IAM role in your AWS account that AI Runtime Control assumes to access Bedrock. See [get Bedrock setup information](https://www.fastly.com/documentation/reference/api/ai-runtime-control/providers#arc-get-bedrock-setup) for the role ARN and external ID your trust policy must reference. | [optional] 
**region** | **str** | The AWS region for Bedrock API requests. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



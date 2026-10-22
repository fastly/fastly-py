# ArcProviderConnectionAwsIam

A provider connection to Amazon Bedrock authenticated with an AWS IAM role. Requires AWS IAM authentication to be enabled on your account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **[str]** | The Bedrock model identifiers this connection is allowed to use. | 
**customer_role_arn** | **str** | The ARN of the IAM role in your AWS account that AI Runtime Control assumes to access Bedrock. See [get Bedrock setup information](https://www.fastly.com/documentation/reference/api/ai-runtime-control/providers#arc-get-bedrock-setup) for the role ARN and external ID your trust policy must reference. | 
**region** | **str** | The AWS region for Bedrock API requests. | 
**name** | **str** | The provider name. Must be `bedrock` for `aws-iam` connections. | defaults to "bedrock"
**auth_type** | **str** | The authentication type for this connection. | defaults to "aws-iam"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



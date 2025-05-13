# DdosProtectionRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **str** | Unique ID of the rule. | [optional] 
**name** | **str** | A human-readable name for the rule. | [optional] 
**action** | [**DdosProtectionAction**](DdosProtectionAction.md) |  | [optional] 
**customer_id** | **str** | Alphanumeric string identifying the customer. | [optional] 
**service_id** | **str** | Alphanumeric string identifying the service. | [optional] 
**source_ip** | **str, none_type** | Source IP address attribute. | [optional] 
**country_code** | **str, none_type** | Country code attribute. | [optional] 
**host** | **str, none_type** | Host attribute. | [optional] 
**asn** | **str, none_type** | ASN attribute. | [optional] 
**source_ip_prefix** | **str, none_type** | Source IP prefix attribute. | [optional] 
**additional_attributes** | **[str]** | Attribute category for additional, unlisted attributes used in a rule. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



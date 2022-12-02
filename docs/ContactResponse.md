# ContactResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str, none_type** | The alphanumeric string representing the user for this customer contact. | [optional] 
**contact_type** | **str** | The type of contact. | [optional] 
**name** | **str, none_type** | The name of this contact, when user_id is not provided. | [optional] 
**email** | **str, none_type** | The email of this contact, when a user_id is not provided. | [optional] 
**phone** | **str, none_type** | The phone number for this contact. Required for primary, technical, and security contact types. | [optional] 
**customer_id** | **str, none_type** | The alphanumeric string representing the customer for this customer contact. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



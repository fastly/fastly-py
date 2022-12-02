# CustomerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_contact_id** | **str, none_type** | The alphanumeric string representing the primary billing contact. | [optional] 
**billing_network_type** | **str** | Customer&#39;s current network revenue type. | [optional] 
**billing_ref** | **str, none_type** | Used for adding purchased orders to customer&#39;s account. | [optional] 
**can_configure_wordpress** | **bool, none_type** | Whether this customer can view or edit wordpress. | [optional] [readonly] 
**can_reset_passwords** | **bool** | Whether this customer can reset passwords. | [optional] [readonly] 
**can_upload_vcl** | **bool** | Whether this customer can upload VCL. | [optional] [readonly] 
**force_2fa** | **bool** | Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled. | [optional] 
**force_sso** | **bool** | Specifies whether SSO is forced or not forced on the customer account. | [optional] 
**has_account_panel** | **bool** | Specifies whether the account has access or does not have access to the account panel. | [optional] 
**has_improved_events** | **bool** | Specifies whether the account has access or does not have access to the improved events. | [optional] 
**has_improved_ssl_config** | **bool** | Whether this customer can view or edit the SSL config. | [optional] [readonly] 
**has_openstack_logging** | **bool** | Specifies whether the account has enabled or not enabled openstack logging. | [optional] 
**has_pci** | **bool** | Specifies whether the account can edit PCI for a service. | [optional] 
**has_pci_passwords** | **bool** | Specifies whether PCI passwords are required for the account. | [optional] [readonly] 
**ip_whitelist** | **str** | The range of IP addresses authorized to access the customer account. | [optional] 
**legal_contact_id** | **str, none_type** | The alphanumeric string identifying the account&#39;s legal contact. | [optional] 
**name** | **str** | The name of the customer, generally the company name. | [optional] 
**owner_id** | **str** | The alphanumeric string identifying the account owner. | [optional] 
**phone_number** | **str** | The phone number associated with the account. | [optional] 
**postal_address** | **str, none_type** | The postal address associated with the account. | [optional] 
**pricing_plan** | **str** | The pricing plan this customer is under. | [optional] 
**pricing_plan_id** | **str** | The alphanumeric string identifying the pricing plan. | [optional] 
**security_contact_id** | **str, none_type** | The alphanumeric string identifying the account&#39;s security contact. | [optional] 
**technical_contact_id** | **str, none_type** | The alphanumeric string identifying the account&#39;s technical contact. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



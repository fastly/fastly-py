# TlsCsrDataAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sans** | **[str]** | Subject Alternate Names - An array of one or more fully qualified domain names or public IP addresses to be secured by this certificate. Required. | 
**common_name** | **str** | Common Name (CN) - The fully qualified domain name (FQDN) to be secured by this certificate. The common name should be one of the entries in the SANs parameter. | [optional] 
**country** | **str** | Country (C) - The two-letter ISO country code where the organization is located. | [optional] 
**state** | **str** | State (S) - The state, province, region, or county where the organization is located. This should not be abbreviated. | [optional] 
**city** | **str** | Locality (L) - The locality, city, town, or village where the organization is located. | [optional] 
**postal_code** | **str** | Postal Code - The postal code where the organization is located. | [optional] 
**street_address** | **str** | Street Address - The street address where the organization is located. | [optional] 
**organization** | **str** | Organization (O) - The legal name of the organization, including any suffixes. This should not be abbreviated. | [optional] 
**organizational_unit** | **str** | Organizational Unit (OU) - The internal division of the organization managing the certificate. | [optional] 
**email** | **str** | Email Address (EMAIL) - The organizational contact for this. | [optional] 
**key_type** | **str** | CSR Key Type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



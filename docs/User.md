# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] [readonly] 
**name** | **str** | The real life name of the user. | [optional] 
**limit_services** | **bool** | Indicates that the user has limited access to the customer&#39;s services. | [optional] 
**locked** | **bool, none_type** | Indicates whether the is account is locked for editing or not. | [optional] 
**require_new_password** | **bool, none_type** | Indicates if a new password is required at next login. | [optional] 
**role** | [**RoleUser**](RoleUser.md) |  | [optional] 
**two_factor_auth_enabled** | **bool, none_type** | Indicates if 2FA is enabled on the user. | [optional] 
**two_factor_setup_required** | **bool** | Indicates if 2FA is required by the user&#39;s customer account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



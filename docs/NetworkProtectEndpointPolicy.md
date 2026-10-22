# NetworkProtectEndpointPolicy

The endpoints serving one network region. Replacing `endpoint_policies` preserves attachment timestamps for the same endpoint and region; reordering does not alter them, while changing preference updates the attachment's `updated_at` value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**NetworkProtectPolicyEndpoints**](NetworkProtectPolicyEndpoints.md) |  | 
**region** | [**NetworkProtectRegion**](NetworkProtectRegion.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



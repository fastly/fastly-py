# LegacyWafFirewall


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_push** | **str** | Date and time that VCL was last pushed to cache nodes. | [optional] 
**prefetch_condition** | **str** | Name of the corresponding condition object. | [optional] 
**response** | **str** | Name of the corresponding response object. | [optional] 
**version** | [**ReadOnlyVersion**](ReadOnlyVersion.md) |  | [optional] 
**service_id** | [**ReadOnlyServiceId**](ReadOnlyServiceId.md) |  | [optional] 
**disabled** | **bool** | The status of the firewall. | [optional]  if omitted the server will use the default value of False
**rule_statuses_log_count** | **int** | The number of rule statuses set to log. | [optional] 
**rule_statuses_block_count** | **int** | The number of rule statuses set to block. | [optional] 
**rule_statuses_disabled_count** | **int** | The number of rule statuses set to disabled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



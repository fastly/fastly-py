# WafFirewallVersionResponseDataAttributesAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether a specific firewall version is currently deployed. | [optional] [readonly] 
**active_rules_fastly_block_count** | **int** | The number of active Fastly rules set to block. | [optional] [readonly] 
**active_rules_fastly_log_count** | **int** | The number of active Fastly rules set to log. | [optional] [readonly] 
**active_rules_fastly_score_count** | **int** | The number of active Fastly rules set to score. | [optional] [readonly] 
**active_rules_owasp_block_count** | **int** | The number of active OWASP rules set to block. | [optional] [readonly] 
**active_rules_owasp_log_count** | **int** | The number of active OWASP rules set to log. | [optional] [readonly] 
**active_rules_owasp_score_count** | **int** | The number of active OWASP rules set to score. | [optional] [readonly] 
**active_rules_trustwave_block_count** | **int** | The number of active Trustwave rules set to block. | [optional] [readonly] 
**active_rules_trustwave_log_count** | **int** | The number of active Trustwave rules set to log. | [optional] [readonly] 
**last_deployment_status** | **str, none_type** | The status of the last deployment of this firewall version. | [optional] [readonly] 
**deployed_at** | **str** | Time-stamp (GMT) indicating when the firewall version was last deployed. | [optional] [readonly] 
**error** | **str** | Contains error message if the firewall version fails to deploy. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



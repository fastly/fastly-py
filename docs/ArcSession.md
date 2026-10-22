# ArcSession

A session log. Other than `firewall_enabled` (always present), `firewall_*` fields are only present when AI Firewall ran on a request in this session. They're absent (not merely empty) otherwise, so their absence and an empty value mean different things. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the session. | [readonly] 
**virtual_key_id** | **str** | The ID of the virtual key used for this session. | 
**model** | **str** | The AI model identifier used. | 
**provider** | **str** | The name of the provider connection that ultimately served the session. | 
**provider_connection_id** | **str** | The ID of the provider connection that ultimately served the session. | 
**requests** | **int** | The number of requests made in this session. | 
**input_tokens** | **int** | The total input tokens consumed in this session. | 
**output_tokens** | **int** | The total output tokens generated in this session. | 
**violations** | **int** | The number of AI Firewall violations detected in this session. | 
**firewall_enabled** | **bool** | Whether AI Firewall was enabled for this session&#39;s virtual key. | 
**created_at** | **datetime** | The date and time the session was created, in RFC 3339 format. | [readonly] 
**updated_at** | **datetime** | The date and time the session was last updated, in RFC 3339 format. | [readonly] 
**logs** | [**[ArcSessionLogEntry]**](ArcSessionLogEntry.md) | The request and response pairs recorded for this session. | 
**virtual_key_name** | **str** | The display name of the virtual key used for this session. | [optional] 
**primary_provider** | **str** | The ID of the provider connection originally requested, before any failover occurred. | [optional] 
**firewall_outcome** | **str** | The outcome AI Firewall reached for this session. Present only when AI Firewall ran. | [optional] 
**firewall_stage** | **str** | The AI Firewall stage that produced the outcome (for example, the request or response stage). Present only when AI Firewall ran. | [optional] 
**firewall_policy** | **str** | The AI Firewall policy that was applied. Present only when AI Firewall ran. | [optional] 
**firewall_incomplete_reason** | **str** | Why AI Firewall inspection was incomplete, if applicable. Present only when AI Firewall ran and inspection didn&#39;t complete. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



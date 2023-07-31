# CacheSettingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | If set, will cause vcl_fetch to terminate after processing this rule with the return state specified. If not set, other configuration logic in vcl_fetch with a lower priority will run after this rule.  | [optional] 
**cache_condition** | **str, none_type** | Name of the cache condition controlling when this configuration applies. | [optional] 
**name** | **str** | Name for the cache settings object. | [optional] 
**stale_ttl** | **str** | Maximum time in seconds to continue to use a stale version of the object if future requests to your backend server fail (also known as &#39;stale if error&#39;). | [optional] 
**ttl** | **str** | Maximum time to consider the object fresh in the cache (the cache &#39;time to live&#39;). | [optional] 
**service_id** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



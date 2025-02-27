# KvStoreUpsertBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the item to be added, updated, retrieved, or deleted. | 
**value** | **str** | Value for the item (in Base64 encoding). | 
**time_to_live_sec** | **int** | Indicates that the item should be deleted after the specified number of seconds have elapsed. Deletion is not immediate but will occur within 24 hours of the requested expiration. | [optional] 
**metadata** | **str** | An arbitrary data field which can contain up to 2000 bytes of data. | [optional] 
**background_fetch** | **bool** | If set to true, the new value for the item will not be immediately visible to other users of the KV store; they will receive the existing (stale) value while the platform updates cached copies. Setting this to true ensures that other users of the KV store will receive responses to &#39;get&#39; operations for this item quickly, although they will be slightly out of date. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **int** | Weight (`1-100`) used to load balance this server against others. | [optional]  if omitted the server will use the default value of 100
**max_conn** | **int** | Maximum number of connections. If the value is `0`, it inherits the value from pool&#39;s `max_conn_default`. | [optional]  if omitted the server will use the default value of 0
**port** | **int** | Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS. | [optional]  if omitted the server will use the default value of 80
**address** | **str** | A hostname, IPv4, or IPv6 address for the server. Required. | [optional] 
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**disabled** | **bool** | Allows servers to be enabled and disabled in a pool. | [optional]  if omitted the server will use the default value of False
**override_host** | **str, none_type** | The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting. | [optional]  if omitted the server will use the default value of "null"
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**service_id** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**pool_id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



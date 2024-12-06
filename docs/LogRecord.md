# LogRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The ID of the Fastly customer that owns the service. | [optional] [readonly] 
**service_id** | [**LogPropertyServiceId**](LogPropertyServiceId.md) |  | [optional] 
**timestamp** | **datetime** | Timestamp of the request in ISO 8601 format. | [optional] 
**client_as_number** | **int** | The autonomous system (AS) number of the client. | [optional] [readonly] 
**client_region** | **str** | The client&#39;s country subdivision code as found in ISO 3166-2. | [optional] [readonly] 
**client_country_code** | **str** | The two-letter ISO 3166-1 country code for the client. | [optional] [readonly] 
**client_os_name** | **str** | The name of the operating system installed on the client device. | [optional] [readonly] 
**client_device_type** | **str** | The type of the client&#39;s device. | [optional] [readonly] 
**client_browser_name** | **str** | The name of the browser in use on the client device. | [optional] [readonly] 
**client_browser_version** | **str** | The version of the browser in use on client device. | [optional] [readonly] 
**fastly_pop** | **str** | The name of the Fastly POP that served this request. | [optional] [readonly] 
**origin_host** | **str** | The name of the origin host that served this request. | [optional] [readonly] 
**request_protocol** | **str** | HTTP protocol version in use for this request. For example, HTTP/1.1. | [optional] [readonly] 
**request_host** | **str** | The name of the request host used for this request. | [optional] [readonly] 
**request_path** | **str** | The URL path supplied for this request. | [optional] [readonly] 
**request_method** | **str** | HTTP method sent by the client such as \&quot;GET\&quot; or \&quot;POST\&quot;. | [optional] [readonly] 
**response_bytes_body** | **int** | Body bytes sent to the client in the response. | [optional] [readonly] 
**response_bytes_header** | **int** | Header bytes sent to the client in the response. | [optional] [readonly] 
**response_content_length** | **int** | Total bytes sent to the client in the response. | [optional] [readonly] 
**response_content_type** | **str** | The content type of the response sent to the client. | [optional] [readonly] 
**response_reason** | **str** | The HTTP reason phrase returned for this request, if any. | [optional] [readonly] 
**response_state** | **str** | The state of the request with optional suffixes describing special cases. | [optional] [readonly] 
**response_status** | **int** | The HTTP response code returned for this request. | [optional] [readonly] 
**response_time** | **float** | The time since the request started in seconds. | [optional] [readonly] 
**response_x_cache** | **str** | Indicates whether the request was a HIT or a MISS. | [optional] [readonly] 
**is_cache_hit** | **bool** | Indicates whether this request was fulfilled from cache. | [optional] [readonly] 
**is_edge** | **bool** | Indicates whether the request was handled by a Fastly edge POP. | [optional] [readonly] 
**is_shield** | **bool** | Indicates whether the request was handled by a Fastly shield POP. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



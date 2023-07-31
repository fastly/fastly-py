# PoolResponseCommon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**between_bytes_timeout** | **str** | Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. | [optional] 
**connect_timeout** | **str** | How long to wait for a timeout in milliseconds. | [optional] 
**first_byte_timeout** | **str** | How long to wait for the first byte in milliseconds. | [optional] 
**max_conn_default** | **str** | Maximum number of connections. | [optional]  if omitted the server will use the default value of "200"
**tls_check_cert** | **str, none_type** | Be strict on checking TLS certs. | [optional] 
**id** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



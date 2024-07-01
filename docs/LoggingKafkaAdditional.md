# LoggingKafkaAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | The Kafka topic to send logs to. Required. | [optional] 
**brokers** | **str** | A comma-separated list of IP addresses or hostnames of Kafka brokers. Required. | [optional] 
**compression_codec** | **str, none_type** | The codec used for compression of your logs. | [optional] 
**required_acks** | **int** | The number of acknowledgements a leader must receive before a write is considered successful. | [optional]  if omitted the server will use the default value of 1
**request_max_bytes** | **int** | The maximum number of bytes sent in one request. Defaults `0` (no limit). | [optional]  if omitted the server will use the default value of 0
**parse_log_keyvals** | **bool** | Enables parsing of key&#x3D;value tuples from the beginning of a logline, turning them into [record headers](https://cwiki.apache.org/confluence/display/KAFKA/KIP-82+-+Add+Record+Headers). | [optional] 
**auth_method** | **str** | SASL authentication method. | [optional] 
**user** | **str** | SASL user. | [optional] 
**password** | **str** | SASL password. | [optional] 
**use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



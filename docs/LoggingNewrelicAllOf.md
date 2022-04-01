# LoggingNewrelicAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **bool, date, datetime, dict, float, int, list, str, none_type** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that New Relic Logs can ingest. | [optional] 
**token** | **str** | The Insert API key from the Account page of your New Relic account. Required. | [optional] 
**region** | **str** | The region to which to stream logs. | [optional]  if omitted the server will use the default value of "US"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



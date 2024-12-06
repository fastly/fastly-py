# LoggingGrafanacloudlogsAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] 
**user** | **str** | The Grafana Cloud Logs Dataset you want to log to. | [optional] 
**url** | **str** | The URL of the Loki instance in your Grafana stack. | [optional] 
**token** | **str** | The Grafana Access Policy token with `logs:write` access scoped to your Loki instance. | [optional] 
**index** | **str** | The Stream Labels, a JSON string used to identify the stream. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



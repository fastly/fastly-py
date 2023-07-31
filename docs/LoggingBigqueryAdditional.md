# LoggingBigqueryAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the BigQuery logging object. Used as a primary key for API access. | [optional] 
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. | [optional] 
**dataset** | **str** | Your BigQuery dataset. | [optional] 
**table** | **str** | Your BigQuery table. | [optional] 
**template_suffix** | **str, none_type** | BigQuery table name suffix template. Optional. | [optional] 
**project_id** | **str** | Your Google Cloud Platform project ID. Required | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



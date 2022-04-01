# LoggingBigqueryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the BigQuery logging object. Used as a primary key for API access. | [optional] 
**placement** | **str, none_type** | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional] 
**format_version** | **int** | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.   | [optional]  if omitted the server will use the default value of 2
**response_condition** | **str, none_type** | The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional] 
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. | [optional] 
**user** | **str** | Your Google Cloud Platform service account email address. The `client_email` field in your service account authentication JSON. Required. | [optional] 
**secret_key** | **str** | Your Google Cloud Platform account secret key. The `private_key` field in your service account authentication JSON. Required. | [optional] 
**dataset** | **str** | Your BigQuery dataset. | [optional] 
**table** | **str** | Your BigQuery table. | [optional] 
**template_suffix** | **str, none_type** | BigQuery table name suffix template. Optional. | [optional] 
**project_id** | **str** | Your Google Cloud Platform project ID. Required | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**service_id** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**version** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



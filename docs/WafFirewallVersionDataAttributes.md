# WafFirewallVersionDataAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_http_versions** | **str** | Allowed HTTP versions. | [optional]  if omitted the server will use the default value of "HTTP/1.0 HTTP/1.1 HTTP/2"
**allowed_methods** | **str** | A space-separated list of HTTP method names. | [optional]  if omitted the server will use the default value of "GET HEAD POST OPTIONS PUT PATCH DELETE"
**allowed_request_content_type** | **str** | Allowed request content types. | [optional]  if omitted the server will use the default value of "application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/x-amf|application/json|text/plain"
**allowed_request_content_type_charset** | **str** | Allowed request content type charset. | [optional]  if omitted the server will use the default value of "utf-8|iso-8859-1|iso-8859-15|windows-1252"
**arg_name_length** | **int** | The maximum allowed argument name length. | [optional]  if omitted the server will use the default value of 100
**arg_length** | **int** | The maximum allowed length of an argument. | [optional]  if omitted the server will use the default value of 400
**combined_file_sizes** | **int** | The maximum allowed size of all files (in bytes). | [optional]  if omitted the server will use the default value of 10000000
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**critical_anomaly_score** | **int** | Score value to add for critical anomalies. | [optional]  if omitted the server will use the default value of 6
**crs_validate_utf8_encoding** | **bool** | CRS validate UTF8 encoding. | [optional] 
**error_anomaly_score** | **int** | Score value to add for error anomalies. | [optional]  if omitted the server will use the default value of 5
**high_risk_country_codes** | **str** | A space-separated list of country codes in ISO 3166-1 (two-letter) format. | [optional] 
**http_violation_score_threshold** | **int** | HTTP violation threshold. | [optional] 
**inbound_anomaly_score_threshold** | **int** | Inbound anomaly threshold. | [optional] 
**lfi_score_threshold** | **int** | Local file inclusion attack threshold. | [optional] 
**locked** | **bool** | Whether a specific firewall version is locked from being modified. | [optional]  if omitted the server will use the default value of False
**max_file_size** | **int** | The maximum allowed file size, in bytes. | [optional]  if omitted the server will use the default value of 10000000
**max_num_args** | **int** | The maximum number of arguments allowed. | [optional]  if omitted the server will use the default value of 255
**notice_anomaly_score** | **int** | Score value to add for notice anomalies. | [optional]  if omitted the server will use the default value of 4
**number** | **int** |  | [optional] [readonly] 
**paranoia_level** | **int** | The configured paranoia level. | [optional]  if omitted the server will use the default value of 1
**php_injection_score_threshold** | **int** | PHP injection threshold. | [optional] 
**rce_score_threshold** | **int** | Remote code execution threshold. | [optional] 
**restricted_extensions** | **str** | A space-separated list of allowed file extensions. | [optional]  if omitted the server will use the default value of ".asa/ .asax/ .ascx/ .axd/ .backup/ .bak/ .bat/ .cdx/ .cer/ .cfg/ .cmd/ .com/ .config/ .conf/ .cs/ .csproj/ .csr/ .dat/ .db/ .dbf/ .dll/ .dos/ .htr/ .htw/ .ida/ .idc/ .idq/ .inc/ .ini/ .key/ .licx/ .lnk/ .log/ .mdb/ .old/ .pass/ .pdb/ .pol/ .printer/ .pwd/ .resources/ .resx/ .sql/ .sys/ .vb/ .vbs/ .vbproj/ .vsdisco/ .webinfo/ .xsd/ .xsx"
**restricted_headers** | **str** | A space-separated list of allowed header names. | [optional]  if omitted the server will use the default value of "/proxy/ /lock-token/ /content-range/ /translate/ /if/"
**rfi_score_threshold** | **int** | Remote file inclusion attack threshold. | [optional] 
**session_fixation_score_threshold** | **int** | Session fixation attack threshold. | [optional] 
**sql_injection_score_threshold** | **int** | SQL injection attack threshold. | [optional] 
**total_arg_length** | **int** | The maximum size of argument names and values. | [optional]  if omitted the server will use the default value of 6400
**warning_anomaly_score** | **int** | Score value to add for warning anomalies. | [optional] 
**xss_score_threshold** | **int** | XSS attack threshold. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



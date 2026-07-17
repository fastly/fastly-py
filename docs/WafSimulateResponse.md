# WafSimulateResponse

Response from the WAF simulation containing the WAF response code and detected signals.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waf_response** | **int** | The HTTP status code the WAF would return for the simulated request (e.g., `200` for allowed, `406` for blocked). | 
**signals** | [**[WafSimulateSignal]**](WafSimulateSignal.md) | List of signals detected by the WAF during simulation. Empty array when no signals are detected. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



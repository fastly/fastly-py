# BillingEstimateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**start_time** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**invoice_id** | **str** |  | [optional] [readonly] 
**customer_id** | **str** |  | [optional] [readonly] 
**vendor_state** | **str** | The current state of our third-party billing vendor. One of `up` or `down`. | [optional] [readonly] 
**status** | [**BillingStatus**](BillingStatus.md) |  | [optional] 
**total** | [**BillingTotal**](BillingTotal.md) |  | [optional] 
**regions** | **{str: ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},)}** | Breakdown of regional data for products that are region based. | [optional] 
**line_items** | [**[BillingEstimateLinesLineItems]**](BillingEstimateLinesLineItems.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



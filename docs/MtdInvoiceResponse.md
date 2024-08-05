# MtdInvoiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The Customer ID associated with the invoice. | [optional] 
**invoice_id** | **str** | An alphanumeric string identifying the invoice. | [optional] 
**billing_start_date** | **datetime** | The date and time (in ISO 8601 format) for the initiation point of a billing cycle, signifying the start of charges for a service or subscription. | [optional] 
**billing_end_date** | **datetime** | The date and time (in ISO 8601 format) for the termination point of a billing cycle, signifying the end of charges for a service or subscription. | [optional] 
**monthly_transaction_amount** | **str** | The total billable amount for invoiced services charged within a single month. | [optional] 
**transaction_line_items** | [**[Mtdlineitems]**](Mtdlineitems.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



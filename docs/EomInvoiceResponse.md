# EomInvoiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID associated with the invoice. | [optional] 
**invoice_id** | **str** | Numeric string identifying the invoice. | [optional] 
**invoice_posted_on** | **datetime** | Date and time invoice was posted on, in ISO 8601 format. | [optional] 
**billing_start_date** | **datetime** | Date and time (in ISO 8601 format) for initiation point of a billing cycle, signifying the start of charges for a service or subscription. | [optional] 
**billing_end_date** | **datetime** | Date and time (in ISO 8601 format) for termination point of a billing cycle, signifying the end of charges for a service or subscription. | [optional] 
**statement_number** | **str** | Alphanumeric string identifying the statement number. | [optional] 
**currency_code** | **str** | Three-letter code representing a specific currency used for financial transactions. | [optional] 
**monthly_transaction_amount** | **float** | Total billable amount for invoiced services charged within a single month. | [optional] 
**transaction_line_items** | [**[Invoicelineitems]**](Invoicelineitems.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



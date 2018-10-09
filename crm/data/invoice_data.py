# -----SO List/Details-----
overwrite_chk = '//input[@name="SO_OVER" and @class="listViewEntriesCheckBox" and @type="radio"]'
overwrite_btn = '//button[contains(., "Overwrite")]'
create_new_btn = '//button[contains(., "Create New")]'

first_so_cell_id = "SalesOrder_listView_row_1"
generate_invoice_id = "SalesOrder_detailView_basicAction_Generate_Invoice"
create_invoice = '//button[@class="btn btn-success"]'
save_button_id = "save_button_id"
invoice_no_id = "Invoice_editView_fieldName_invoice_no"
so_cell_path = '//tr//td[contains(.,"S50269")]'
customer_po_id = "Invoice_editView_fieldName_subject"
customer_no_id = "Invoice_editView_fieldName_customerno"
contact_name_id = "Invoice_editView_fieldName_contact_id_select"
terms_of_sale_id = "tsale__chzn"

qa_terms_of_sale = '//li[contains(.,"Pre-payment")]'
tst_terms_of_sale = '//li[contains(.,"NET-30")]'

terms_of_delivery_id = "tdelivery__chzn"
terms_of_delivery = '//li[contains(.,"CIP")]'

sales_commission_id = "Invoice_editView_fieldName_salescommission"
account_id = "Invoice_editView_fieldName_accarrier"
boxes_id = "Invoice_editView_fieldName_inv_box"
dimensions_id = "Invoice_editView_fieldName_inv_demension"
due_date_id = "Invoice_editView_fieldName_duedate"
territory_id = "territory__chzn"
territory = '//li[contains(.,"EES")]'

status_id = "invoicestatus__chzn"
qa_status = '//li[contains(.,"Unpaid")]'
tst_status = '//li[contains(.,"Unpaid")]'

# Assigned To - need ID
assigned_to = '//li[contains(.,"Administrator")]'
priority_id = "rpriority__chzn"
priority = '//li[contains(.,"Routine")]'

place_of_delivery_id = "Invoice_editView_fieldName_pdelivery"
ship_via_id="carrier__chzn"
ship_via = '//li[contains(.,"FEDEX")]'

awb_id = "Invoice_editView_fieldName_awb"
weight_id = "Invoice_editView_fieldName_inv_weight"
invoice_date_id = "Invoice_editView_fieldName_invoicedate"
order_date_id = "Invoice_editView_fieldName_orderdate"
# Custom information
total_payment_id = "Invoice_editView_fieldName_cf_total_payments"
percent_paid_id = "Invoice_editView_fieldName_cf_percent_paid"

special_notes_id = "Invoice_editView_fieldName_specialnotes"

# finally url
after_creation_url = 'http://crmtst_us.bai-inc.eu/index.php?module=Invoice&view=Detail&record'
invoice_details = '//li(@class[contains("Invoice Details")])'


billing_address_id = "Invoice_editView_fieldName_bill_street"
billing_po_box_id = "Invoice_editView_fieldName_bill_pobox"
billing_city_id = "Invoice_editView_fieldName_bill_city"
billing_state_id = "Invoice_editView_fieldName_bill_state"
billing_post_code_id = "Invoice_editView_fieldName_bill_code"
billing_country_id = "Invoice_editView_fieldName_bill_country"
shipping_address_id = "Invoice_editView_fieldName_ship_street"
shipping_po_box_id = "Invoice_editView_fieldName_ship_pobox"
shipping_city_id = "Invoice_editView_fieldName_ship_city"
shipping_state_id = "Invoice_editView_fieldName_ship_state"
shipping_post_code_id = "Invoice_editView_fieldName_ship_code"
shipping_country_id = "Invoice_editView_fieldName_ship_country"


billing_address = "Invoice_detailView_fieldValue_bill_street"
billing_po_box = "Invoice_detailView_fieldValue_bill_pobox"
billing_city = "Invoice_detailView_fieldValue_bill_city"
billing_state = "Invoice_detailView_fieldValue_bill_state"
billing_post_code = "Invoice_detailView_fieldValue_bill_code"
billing_country = "Invoice_detailView_fieldValue_bill_country"
shipping_address = "Invoice_detailView_fieldValue_ship_street"
shipping_po_box = "Invoice_detailView_fieldValue_ship_pobox"
shipping_city = "Invoice_detailView_fieldValue_ship_city"
shipping_state = "Invoice_detailView_fieldValue_ship_state"
shipping_country = "Invoice_detailView_fieldValue_ship_country"
shipping_post_code = "Invoice_detailView_fieldValue_ship_code"

# Purchase Order XPATH's
expected_url = "index.php?module=PurchaseOrder&view=Edit"
required_field_error = '//div[@class="formErrorContent"]'
actions = '//button[contains(.,"Actions")]'

product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products" and @data-module-name="Products"]'

# Purchase Order list ID's

pdf_export_id = "PurchaseOrder_listView_massAction_PDF_Export"
edit_po_id = "PurchaseOrder_listView_massAction_LBL_EDIT"
delete_po_id = "PurchaseOrder_listView_massAction_LBL_DELETE"
import_po_id = "PurchaseOrder_listView_advancedAction_LBL_IMPORT"
export_po_id = "PurchaseOrder_listView_advancedAction_LBL_EXPORT"
add_po_id = "PurchaseOrder_listView_basicAction_LBL_ADD_RECORD"

# Purchase Order profile XPATH's
vendor_address_field = '//textarea[@class="row-fluid " and @name="bill_street"]'
shipping_address_field = '//textarea @class="row-fluid " and @name="ship_street"]'
copy_vendor_address = '//a[contains(.,"Copy Vendor Address")]'
copy_company_address = '//a[contains(.,"Copy Company Address")]'

# Purchase Order profile ID's

save_button_id = "save_but"
add_po_id = "PurchaseOrder_listView_basicAction_LBL_ADD_RECORD"
po_vendor_list_id = "PurchaseOrder_editView_fieldName_vendor_id_select"
excise_duty_id = "PurchaseOrder_editView_fieldName_exciseduty"
assigned_to_id = "selA7H_chzn"
terms_of_delivery_id = "tdelivery__chzn"
territory_id = "territory__chzn"
location_id = "PurchaseOrder_editView_fieldName_locationid_select"

# Profile fields
vendor_po_id = "PurchaseOrder_editView_fieldName_subject"
tracking_number_id = "PurchaseOrder_editView_fieldName_tracking_no"
priority_id = "rpriority__chzn"
account_id = "PurchaseOrder_editView_fieldName_accarrier"
status_id = "postatus__chzn"
terms_of_payment_id = "tsale__chzn"
place_of_delivery_id = "PurchaseOrder_editView_fieldName_pdelivery"
po_number_id = "PurchaseOrder_editView_fieldName_purchaseorder_no"
requisition_number_id = "PurchaseOrder_editView_fieldName_requisition_no"
contact_name_id = "PurchaseOrder_editView_fieldName_contact_id_select"
ship_via_id = "carrier__chzn"
sales_commission_id = "PurchaseOrder_editView_fieldName_salescommission"
aircraft_id = "PurchaseOrder_editView_fieldName_fleetid_select"
due_date_id = "PurchaseOrder_editView_fieldName_duedate"

po_risk_id = "risk__chzn"
low_risk_value = '//a[contains(., "Low")]'

vendor_po_box_id = "PurchaseOrder_editView_fieldName_bill_pobox"
vendor_city_id = "PurchaseOrder_editView_fieldName_bill_city"
vendor_state_id = "PurchaseOrder_editView_fieldName_bill_state"
vendor_post_code_id = "PurchaseOrder_editView_fieldName_bill_code"
vendor_country_id = "PurchaseOrder_editView_fieldName_bill_country"
shipping_po_box_id = "PurchaseOrder_editView_fieldName_ship_pobox"
shipping_city_id = "PurchaseOrder_editView_fieldName_ship_city"
shipping_state_id = "PurchaseOrder_editView_fieldName_ship_state"
shipping_postal_code_id = "PurchaseOrder_editView_fieldName_ship_code"
shipping_country_id = "PurchaseOrder_editView_fieldName_ship_country"


# description_details_id = "form-validation-field-0"

description_details_field = '//textarea[@name="description")]'

# Fields values
priority = '//li[contains(.,"Routine")]'
status = '//li[contains(.,"Approved")]'
tst_terms_of_payment = '//li[contains(.,"NET-30")]'
qa_terms_of_payment = '//li[contains(.,"Pre-payment")]'
ship_via = '//li[contains(.,"DHL")]'
assigned_to = '//li[contains(.,"EEO")]'
terms_of_delivery = '//li[contains(.,"CFR")]'
territory = '//li[contains(.,"EES")]'


pn_field_id = "productName1"
# Additional data

expected_url = "index.php?module=SalesOrder&view=Edit"

# XPATH's
required_field_error = '//div[@class="formErrorContent"]'
actions = '//button[contains(.,"Actions")]'
account_info_dialog_no = '//a[contains(.,"No")]'
account_info_dialog_yes = '//a[contains(.,"Yes")]'

# Sales Order list ID's

pdf_export_id = "SalesOrder_listView_massAction_PDF_Export"
edit_so_id = "SalesOrder_listView_massAction_LBL_EDIT"
delete_so_id = "SalesOrder_listView_massAction_LBL_DELETE"
import_so_id = "SalesOrder_listView_advancedAction_LBL_IMPORT"
export_so_id = "SalesOrder_listView_advancedAction_LBL_EXPORT"
add_so_id = "SalesOrder_listView_basicAction_LBL_ADD_RECORD"

place_of_delivery_id = "SalesOrder_editView_fieldName_pdelivery"

# Sales Order profile XPATH's
save_so_button_id = "save_but"
created_status = '//li[@class[contains(.,"Created")]'
#   Values
terms_of_delivery_value = '//li[@class[contains(.,"CIP")]'
territory_value = "//li[contains(., 'EES')]"
status_approved_value = '//li[contains(.,"Approved")]'
terms_of_delivery_value = '//li[contains(.,"CFR")]'
terms_of_payment_value = '//li[contains(.,"NET-60")]'
assigned_to_value = '//li[contains(.,"EEO")]'
priority_value = '//li[contains(.,"Routine")]'
ship_via_value = '//li[contains(.,"FEDEX")]'
contact_name_overwrite_adress = '//a[contains(.,"No")]'
terms_of_payment_id = "tsale__chzn"
priority_id = "rpriority__chzn"
terms_of_sale_value = '//li[contains(.,"NET-30")]'
source_value = '//li[contains(.,"Fax")]'
item_selector = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @data-popup="ProductsPopup"]'
copy_billing_address_from_contact_left = '//input[@name="copyAddressFromRight" and @class="contactAddress"]'
copy_billing_address_from_account_left = '//input[@name="copyAddressFromRight" and @class="accountAddress"]'
copy_billing_address_from_shipping_address_left = '//input[@name="copyAddressFromRight" @class="shippingAddress"]'
copy_billing_address_from_contact_right = '//input[@name="copyAddressFromLeft" and @class="contactAddress"]'
copy_billing_address_from_account_right = '//input[@name="copyAddressFromLeft" and @class="accountAddress"]'
copy_billing_address_from_shipping_address_right = '//input[@name="copyAddressFromLeft" and @class="shippingAddress"]'

product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products"]'

#   Edit Sales Order profile ID's

save_button_id = "save_but"
client_po_id = "SalesOrder_editView_fieldName_subject"
so_number_id = "SalesOrder_editView_fieldName_salesorder_no"
contact_name_selector_id = "SalesOrder_editView_fieldName_contact_id_select"
ship_via_selector_id = "carrier__chzn"
status_selector_id = "sostatus__chzn"
sales_commission_id = "SalesOrder_editView_fieldName_salescommission"
assigned_to_selector_id = "assigned_user_id_chzn"
terms_of_delivery_selector_id = "tdelivery__chzn"
territory_selector_id = "territory__chzn"
location_selector_id = "SalesOrder_editView_fieldName_locationid_select"
account_selector_id = "SalesOrder_editView_fieldName_account_id_select"
account_num_id = "SalesOrder_editView_fieldName_accarrier"
account_id = "SalesOrder_editView_fieldName_account_id_select"
assets_id = "SalesOrder_editView_fieldName_assestid_select"
sold_by_id = "SalesOrder_editView_fieldName_soldbyid_select"
aircraft_id = "SalesOrder_editView_fieldName_fleetid_select"
customer_quote_id = "SalesOrder_editView_fieldName_quote_id_select"
account_id_display_id = "account_id_display"

billing_address_id = "SalesOrder_editView_fieldName_bill_street"
billing_po_box_id = "SalesOrder_editView_fieldName_bill_pobox"
billing_city_id = "SalesOrder_editView_fieldName_bill_city"
billing_state_id = "SalesOrder_editView_fieldName_bill_state"
billing_post_code_id = "SalesOrder_editView_fieldName_bill_code"
billing_country_id = "SalesOrder_editView_fieldName_bill_country"
shipping_address_id = "SalesOrder_editView_fieldName_ship_street"
shipping_po_box_id = "SalesOrder_editView_fieldName_ship_pobox"
shipping_city_id = "SalesOrder_editView_fieldName_ship_city"
shipping_state_id = "SalesOrder_editView_fieldName_ship_state"
shipping_post_code_id = "SalesOrder_editView_fieldName_ship_code"
shipping_country_id = "SalesOrder_editView_fieldName_ship_country"

part_number_field_id = "products_popup"

terms_and_conditions_id = "SalesOrder_editView_fieldName_terms_conditions"
notes_id = "SalesOrder_editView_fieldName_description"

#   Details Sales Order profile ID's
client_po = "SalesOrder_detailView_fieldValue_subject"
so_numbers = "SalesOrder_detailView_fieldValue_salesorder_no"
contact_name = "SalesOrder_detailView_fieldValue_contact_id"
ship_via = "SalesOrder_detailView_fieldValue_carrier"
status = "SalesOrder_detailView_fieldValue_sostatus"
sales_commission = "SalesOrder_detailView_fieldValue_salescommission"
assigned_to = "SalesOrder_detailView_fieldValue_assigned_user_id"
modified_time = "SalesOrder_detailView_fieldValue_modifiedtime"
terms_of_delivery = "SalesOrder_detailView_fieldValue_tdelivery"
created_by = "SalesOrder_detailView_fieldValue_create_user_id"
aircraft = "SalesOrder_detailView_fieldValue_fleetid"
sold_by = "SalesOrder_detailView_fieldValue_soldbyid"

customer_order_date = "SalesOrder_detailView_fieldValue_customerdate"
customer_quote = "SalesOrder_detailView_fieldValue_quote_id"
ue_date = "SalesOrder_detailView_fieldValue_duedate"
priority = "SalesOrder_detailView_fieldValue_rpriority"
account_num = "SalesOrder_detailView_fieldValue_accarrier"
account = "SalesOrder_detailView_fieldValue_account_id"
created_time = "SalesOrder_detailView_fieldValue_createdtime"
terms_of_sale = "SalesOrder_detailView_fieldValue_tsale"

place_of_delivery = "SalesOrder_detailView_fieldValue_pdelivery"
territory = "SalesOrder_detailView_fieldValue_territory"
location = "SalesOrder_detailView_fieldValue_locationid"
assets = "SalesOrder_detailView_fieldValue_assestid"

billing_address = "SalesOrder_detailView_fieldValue_bill_street"
billing_po_box = "SalesOrder_detailView_fieldValue_bill_pobox"
billing_city = "SalesOrder_detailView_fieldValue_bill_city"
billing_state = "SalesOrder_detailView_fieldValue_bill_state"
billing_post_code = "SalesOrder_detailView_fieldValue_bill_code"
billing_country = "SalesOrder_detailView_fieldValue_bill_country"
shipping_address = "SalesOrder_detailView_fieldValue_ship_street"
shipping_po_box = "SalesOrder_detailView_fieldValue_ship_pobox"
shipping_city = "SalesOrder_detailView_fieldValue_ship_city"
shipping_state = "SalesOrder_detailView_fieldValue_ship_state"
shipping_country = "SalesOrder_detailView_fieldValue_ship_country"
shipping_post_code = "SalesOrder_detailView_fieldValue_ship_code"
source_details = "SalesOrder_detailView_fieldValue_docsource"
sub_total_id = "netTotal"
grand_total_id = "grandTotal"

terms_of_sale_id = "tsale__chzn"
source_id = "docsource__chzn"

from_stock_1_id = "fromstock1"
from_stock_2_id = "fromstock2"
from_stock_3_id = "fromstock3"

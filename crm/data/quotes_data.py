expected_url = "index.php?module=Quotes&view=Edit"

#product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products"]'
product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @data-module-name="Products" and @title="Products"]'
#product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products"]'
# Quotes Order XPATH's

required_field_error = '//div[@class="formErrorContent"]'
actions = '//button[contains(.,"Actions")]'

quote_stage = '//li[contains(.,"In Progress")]'
priority = '//li[contains(.,"Routine")]'
terms_of_delivery = '//li[contains(.,"CFR")]'
terms_of_sale = '//li[contains(.,"Pre-payment")]'

# Quotes Order list ID's

pdf_export_id = "Quotes_listView_massAction_PDF_Export"
edit_quote_id = "Quotes_listView_massAction_LBL_EDIT"
delete_quote_id = "Quotes_listView_massAction_LBL_DELETE"
import_quote_id = "Quotes_listView_advancedAction_LBL_IMPORT"
export_quote_id = "Quotes_listView_advancedAction_LBL_EXPORT"
add_quote_id = "Quotes_listView_basicAction_LBL_ADD_RECORD"

# Purchase Order profile XPATH's


# Purchase Order profile ID's

add_quote_id = "Quotes_listView_basicAction_LBL_ADD_RECORD"
account_selector_id = "Quotes_editView_fieldName_account_id_select"
assigned_to_selector_id = "selPB0_chzn"
billing_address_id = "Quotes_editView_fieldName_bill_street"
shipping_address_id="Quotes_editView_fieldName_ship_street"
quote_description_details_id = "Quotes_editView_fieldName_description"
save_quote_button_id = "save_but"

quote_stage_id = "quotestage__chzn"
priority_id = "rpriority__chzn"
terms_of_delivery_id = "tdelivery__chzn"
terms_of_sale_id = "tsale__chzn"

cust_ref_id = "Quotes_editView_fieldName_subject"
place_of_delivery_id = "Quotes_editView_fieldName_pdelivery"

billing_address_id = "Quotes_editView_fieldName_bill_street"  # required
billing_po_box_id = "Quotes_editView_fieldName_bill_pobox"
billing_city_id = "Quotes_editView_fieldName_bill_city"
billing_state_id = "Quotes_editView_fieldName_bill_state"
billing_post_code_id = "Quotes_editView_fieldName_bill_code"
billing_country_id = "Quotes_editView_fieldName_bill_country"
shipping_address_id = "Quotes_editView_fieldName_ship_street"  # required
shipping_po_box_id = "Quotes_editView_fieldName_ship_pobox"
shipping_city_id = "Quotes_editView_fieldName_ship_city"
shipping_state_id = "Quotes_editView_fieldName_ship_state"
shipping_post_code_id = "Quotes_editView_fieldName_ship_code"
shipping_country_id = "Quotes_editView_fieldName_ship_country"

expected_url = "index.php?module=Quotes&view=Edit"

# product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products"]'
product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @data-module-name="Products" and @title="Products"]'
# product_list_button = '//img[@class="lineItemPopup cursorPointer alignMiddle" and @title="Products"]'
# Quotes Order XPATH's

required_field_error = '//div[@class="formErrorContent"]'
actions = '//button[contains(.,"Actions")]'

territory_id = "territory__chzn"

qa_quote_stage = '//li[contains(.,"Accepted")]'
tst_quote_stage = '//li[contains(.,"Accepted")]'
priority = '//li[contains(.,"Routine")]'
terms_of_delivery = '//li[contains(.,"CFR")]'
qa_terms_of_sale = '//li[contains(.,"NET-30")]'
tst_terms_of_sale = '//li[contains(.,"NET-30")]'

# Quotes details
edit_quote_button_id = "Quotes_detailView_basicAction_LBL_EDIT"

# Quotes Order list ID's

pdf_export_id = "Quotes_listView_massAction_PDF_Export"
edit_quote_id = "Quotes_listView_massAction_LBL_EDIT"
delete_quote_id = "Quotes_listView_massAction_LBL_DELETE"
import_quote_id = "Quotes_listView_advancedAction_LBL_IMPORT"
export_quote_id = "Quotes_listView_advancedAction_LBL_EXPORT"
add_quote_id = "Quotes_listView_basicAction_LBL_ADD_RECORD"

# Quote profile XPATH's

territory_ees_value = "//li[contains(., 'EES')]"
territory_bann_i_value = "//li[contains(., 'BANN-EES-I')]"
territory_bann_d_value = "//li[contains(., 'BANN-EES-D')]"

# Quote profile ID's

add_quote_id = "Quotes_listView_basicAction_LBL_ADD_RECORD"
account_selector_id = "Quotes_editView_fieldName_account_id_select"
account_display_id = "account_id_display"
assigned_to_selector_id = "Quotes_editView_fieldName_account_id_select"
billing_address_id = "Quotes_editView_fieldName_bill_street"
shipping_address_id="Quotes_editView_fieldName_ship_street"
quote_description_details_id = "Quotes_editView_fieldName_description"
save_quote_button_id = "save_but"

delivery_edit_id = "Quotes_editView_fieldName_leadtime"
delivery_details_id = "Quotes_detailView_fieldName_leadtime"
quote_stage_id = "quotestage__chzn"
priority_id = "rpriority__chzn"
terms_of_delivery_id = "tdelivery__chzn"
terms_of_sale_id = "tsale__chzn"
terms_of_sale = "Quotes_detailView_fieldValue_tsale"

cust_ref_id = "Quotes_editView_fieldName_subject"
place_of_delivery_edit_id = "Quotes_editView_fieldName_pdelivery"
aircraft_edit_id = "fleetid_display"
location_edit_id = "locationid_display"

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

billing_address = "Quotes_detailView_fieldValue_bill_street"
billing_po_box = "Quotes_detailView_fieldValue_bill_pobox"
billing_city = "Quotes_detailView_fieldValue_bill_city"
billing_state = "Quotes_detailView_fieldValue_bill_state"
billing_post_code = "Quotes_detailView_fieldValue_bill_code"
billing_country = "Quotes_detailView_fieldValue_bill_country"
shipping_address = "Quotes_detailView_fieldValue_ship_street"
shipping_po_box = "Quotes_detailView_fieldValue_ship_pobox"
shipping_city = "Quotes_detailView_fieldValue_ship_city"
shipping_state = "Quotes_detailView_fieldValue_ship_state"
shipping_country = "Quotes_detailView_fieldValue_ship_country"
shipping_post_code = "Quotes_detailView_fieldValue_ship_code"

account = "Quotes_detailView_fieldValue_account_id"
location = "Quotes_detailView_fieldValue_locationid"
aircraft = "Quotes_detailView_fieldValue_fleetid"
quoted_by = "Quotes_detailView_fieldValue_assigned_user_id1"
aircraft_selector_id = "Quotes_editView_fieldName_fleetid_select"
location_selector_id = "Quotes_editView_fieldName_locationid_select"
cust_ref_details_id = "Quotes_detailView_fieldValue_subject"
location_details_id = "Quotes_detailView_fieldValue_locationid"
aircraft_details_id = "Quotes_detailView_fieldValue_fleetid"

terms_of_delivery_details_id = "Quotes_detailView_fieldValue_tdelivery"
terms_of_sale_details_id = "Quotes_detailView_fieldValue_tsale"

quote_number_details_id = "Quotes_detailView_fieldValue_quote_no"
condition_details_id = "Quotes_detailView_fieldValue_condition"
assigned_to_details_id = "Quotes_detailView_fieldValue_assigned_user_id"
territory_details_id = "Quotes_detailView_fieldValue_territory"
quote_stage_details_id = "Quotes_detailView_fieldValue_quotestage"
priority_details_id = "Quotes_detailView_fieldValue_rpriority"
qb_company_details_id = "Quotes_detailView_fieldValue_cf_qb_company"
qb_class_details_id = "Quotes_detailView_fieldValue_cf_qb_class"
place_of_delivery_details_id = "Quotes_detailView_fieldValue_pdelivery"

cancel_quote_id = "cancelLink"

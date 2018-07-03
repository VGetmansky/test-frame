# -----Additional data-----
#http://crmtst_us.bai-inc.eu/index.php?module=Rfq&view=List
expected_url = "index.php?module=Rfq&view=Edit"


# XPATH's
required_field_error = '//div[@class="formErrorContent"]'
actions = '//button[contains(.,"Actions")]'


# -----RFQ list ID's-----
pdf_export_id = "Rfq_listView_massAction_PDF_Export"
edit_rfq_id = "Rfq_listView_massAction_LBL_EDIT"
delete_rfq_id = "Rfq_listView_massAction_LBL_DELETE"
import_rfq_id = "Rfq_listView_advancedAction_LBL_IMPORT"
export_rfq_id = "Rfq_listView_advancedAction_LBL_EXPORT"
add_rfq_id = "Rfq_listView_basicAction_LBL_ADD_RECORD"
vendor_list_id = "vendor_searh"

created_by_id = "s2id_autogen5"
created_by_id1 = "s2id_autogen15"

search_button = '//button[contains(.,"Search")]'


# -----RFQ Profile-----
save_rfq_id = "save_rfq"
partlist_description = '//input[@class="standart-input-inputitem" and @name="noun_1_1"]' # "form-validation-field-0"

add_part_line_id = "add_pl_button"
partnumber_id = "pl_ins_pn"
partnumber_qty_id = "pl_ins_qty"
insert_part_number_id = "pl_ins_but"


# -----Information/Address-----
rfq_account_id = "Rfq_editView_fieldName_account_id_select"
rfq_contact_id = "Rfq_editView_fieldName_parent_id_select"
rfq_vendor_id = "vendor_searh"
contact_id = "ui-id-5"
contact = '//li[contains(., "Autotest User")]'

# -----Information/Address details-----
rfq_aircraft_id = "Rfq_editView_fieldName_fleetid_select"
rfq_location_id = "locationid_display"


# Rfq tabs
information_address_tab_id = "tab_1"
information_details_id = "target_tab_1"
parts_list_id = "tab_2"
parts_list_details_id = "target_tab_2"

# -----Parts List details-----
history_tab_id = "history_tab"
h_payment_terms_id = "terms_of_payment"
h_delivery_terms_id = "terms_of_delivery"
h_vendor_code_id = "vendor_code_2"

ils_tab_id = "searches_tab"
ils_sales_name_id = "sales_name"
ils_phone_id = "phone_name"
ils_fax_id = "fax_name"
ils_email_id = "email_name"
ils_address_id = "adress_name"

recent_quotes_tab_id = "recent_tab"
rq_vendor_code_id = "vendor_code_2"

catalogs_tab_id = "catalogs_tab"

sites_tab_id = "sites_tab"
s_name_id = "sales_name"
s_phone_id = "phone_name"
s_fax_id = "fax_name"
s_email_id = "email_name"
s_address_id = "adress_name"
s_payment_terms_id="terms_of_payment"
s_rq_delivery_terms_id = "terms_of_delivery"
s_vendor_code_id = "vendor_code_2"

inventory_tab_id = "inventory_tab"


customer_quote_id = "Rfq_editView_fieldName_subject"
experation_date_id = "Rfq_editView_fieldName_experationdate"
received_via_id = "Rfq_editView_fieldName_quotefrom"
sale_terms_id = "tsale__chzn"
delivery_terms_id = "tdelivery__chzn"
delivery_terms_field_id = "Rfq_editView_fieldName_pdelivery"
description_id = "Rfq_editView_fieldName_description"
territory_id = "territory__chzn"
territory = '//li[contains(.,"EES")]'
assigned_to_id = "assigned_user_id_chzn"
assigned_to = '//li[contains(.,"Administrator")]'
date_id = "Rfq_editView_fieldName_rfqdate"
priority_id = "rpriority__chzn"
priority = '//li[contains(.,"Routine")]'

sale_terms = '//li[contains(.,"Pre-payment")]'
delivery_terms = '//li[contains(.,"CIF")]'

pl_status_id = "rfqstatus__chzn"
pl_status = '//li[contains(.,"Planning")]'

# -----Req Line Information-----
rli_wa_chkbox = '//label[contains(.,"wa_check")]'
rli_nq_chkbox = '//label[contains(.,"nq_check")]'

pn_req_id = "pn_req"
rli_nsn_id = "req_nsn"
rli_description_id = "req_description"
rli_choose_description = '//div[contains(.,"Choose description")]'
rli_qty_req_id = "qty_req"
rli_uom_id = "req_uom_chzn"
rli_condition_id="pn_condition_chzn"
rli_saved_price_id = "save_price"

# -----Selected Part List Information-----
spli_vendor_name_id = "vendor_name"
spli_vendor_search_id = "vendor_searh"
spli_pn_aval_id = "pn_aval"
spli_sales_type_id = "pn_salestype"
spli_description_id = "form-validation-field-0"
spli_tags_id = "tags_arrow"
spli_rate_id = "outright_ratio"
spli_aval_qty_id = "pn_aqty"
spli_uom_id = "pn_uom_chzn"
spli_condition_id = "pn_condition_chzn"
spli_location_id = "pn_location"

pn_description_id = "pn_description"

# -----Offer Line-----
offer_id = "btn_offer"
alt_offer_id = "btn_altoffer"
save_pricing_id = "btn_saveprice"
save_and_offer_id = "btn_save_offer"
save_and_alt_offer_id = "btn_save_altofer"
create_new_line = '//a[contains(., "Create New line")]'

# -----Stock Outright-----
nq_line_id = "velosiped"
unit_cost_id = "unit_cost"
stock_out_unit_price_id = "unit_price"
vendor_moq_id = "vendor_moq"
moq_id = "pl_moq"
stock_out_unit_price_id = "unit_price"
stock_out_min_vendor_order_id = "minimum_vendor_order"
stock_out_qty_id = "quantity"
total_cost_id = "toral_cost"
total_price_id = "total_price"
stock_out_lead_time_id = "leadtime"
stock_out_delivery_time_id = "delivery_time"
mgm_id = "pl_mgm"
mgm_percent_id = "mgm_percent_outright"


# -----Exchange-----
ex_fee_cost_id = "exchange_fee_cost"
ex_service_cost_id = "exchange_service_cost"
ex_vendor_rtnr_days_id = "exchange_rtrn_day"
ex_ber_cost_id = "exchange_ber_cost"
ex_lead_time_id = "exchange_leadtime"
ex_cost_total_id = "exchange_total_cost"
ex_qty_id = "exchange_qty"
ex_fee_price_id = "exchange_fee_price"
ex_cust_rtnr_days_id = "exchange_rtrn_priceday"
ex_service_price_id = "exchange_service_price"
ex_ber_price_id = "exchange_ber_price"
ex_total_id = "exchange_total_price"
ex_mgm_id = "exchange_mgm"
ex_mgm_percent_id = "mgm_percent_exchange"
ex_delivery_time_id = "exchange_deliverytime"


# -----Repair/OH-----
b_check_cost_id = "repair_bcost"
lead_b_check_id = "repair_bcheck"
mgm_percent_repair_id = "mgm_percent_repair"
avg_repair_cost_id = "repair_avg_cost"
max_repair_cost_id = "repair_max_cost"
repair_lead_time_id = "repair_leadtime"
repair_qty_id = "repair_qty"
repair_b_check_price_id = "repair_bprice"
repair_delivery_b_check_id = "repair_bcheck_price"
avg_repair_price_id = "repair_avg_price"
max_repair_price_id = "repair_max_price"
repair_delivery_time_id="repair_deliverytime"
repair_mgm_id = "repair_mgm_price"
repair_mgm_percent_id = "mgm_percent_repair"

rfq_create_quote_id = "Rfq_detailView_basicAction_LBL_CREATEQUOTE"
# -----Notes I/c & V.Quote-----
notes_id = "notes"
non_printed_notes_id = "np_notes"
i_c_id = "ICHG_chzn"
i_c = '//li[contains(.,"Full")]'  # "One Way"/"PMA"
v_quote_id = "vquote"
v_quote_date_id = "vqdate"

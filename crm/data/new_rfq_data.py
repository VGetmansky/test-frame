new_qa_rfq_url = 'https://crmqa.bai-inc.eu/crm/#/rfq/'
new_qa_dev_rfq_url = 'https://crmqa.bai-inc.eu/crmqa/#/rfq/'
new_tst_rfq_url = 'https://crmtst.bai-inc.eu/crm/#/rfq/'
new_rfq_title = 'New RFQ'

add_rfq_id = "Rfq_listView_basicAction_LBL_ADD_RECORD"

#   ----------  Information / Address   ----------

rfq_number_id = "rfq-number"

rfq_search_account_id = "rfq-search-account"
rfq_search_contact_id = "rfq-search-contact"

rfq_search_value_id = "search-value"
rfq_account_search_button_id = "search-button"

rfq_account_first_field = "//td[contains(., 'Account for autotests')]"
rfq_contact_first_field = "//td[contains(., 'Autotest')]"
rfq_account_id = "rfq-account"
rfq_contact_id = "rfq-contact"

rfq_priority_id = "rfq-priority"
rfq_routine_proirity = '//li[contains(., "Routine")]'
rfq_planning_status = '//li[contains(., "Planning")]'

rfq_tst_sale_terms = '//li[contains(., "NET-30")]'
rfq_qa_sale_terms = '//li[contains(.,"NET-30")]'
rfq_delivery_terms = '//li[contains(.,"CIF")]'

#   ----------  Details  ----------

rfq_customer_quote_id = "rfq-customer-quote"
rfq_expiration_date_id = "rfq-experation-date"
rfq_received_via_id = "rfq-received-via"
rfq_terms_of_sale_id = "rfq-tsale"
rfq_terms_of_delivery_id = "rfq-tdelivery"
rfq_place_of_delivery_id = "rfq-pdelivery"
rfq_description_id = "rfq-description"
rfq_territory_id = "rfq-territory"
rfq_assigned_to_id = "rfq-assigned"
rfq_assigned_to = "//li[contains(., 'Administrator')]"
rfq_aircraft_id = "rfq-aircraft"
rfq_location_id = "rfq-location"

#   ----------  Parts list   ----------

rfq_status_id = "rfq-status"
rfq_created_status = "//li[contains(., 'Created')]"
rfq_add_part_id = "rfq-add-part"
rfq_part_add_multi_id = "part-add-multi"
add_part_alt_id = "rfq-add-alt"
rfq_add_to_list_button_id = "rfq-add-to-list"
rfq_change_mode_id = "rfq-change-mode"
part_number_cell_0_id = "part-add-number-0"
description_cell_0_id = "part-add-desc-0"
qty_cell_0_id = "part-add-qty-0"


#   ----------  REQ LINE INFORMATION  ----------

rfq_pn_req_id = "rfq-pn-req"
rfq_req_description_id = "rfq-req-description"
rfq_nsn_id = "rfq-req-nsn"
rfq_sales_type_id = "rfq-req-sales-type"
rfq_qty_req_id = "rfq-req-qty"
rfq_req_uom_id = "rfq-req-uom"
rfq_req_condition_id = "rfq-req-condition"
rfq_will_advice_check_id = "rfq-part-will-advice"

#   ----------  Buttons ----------

rfq_pn_offer_id = "rfq-offer"
rfq_pn_alt_offer_id = "rfq-alt-offer"
rfq_pn_save_pricing_id = "rfq-save-pricing"
rfq_pn_save_and_offer_id = "rfq-save-offer"
rfq_pn_save_and_alt_offer_id = "rfq-save-alt-offer"
rfq_nq_line_id = "rfq-nq-line"

#   ----------  Part Line Information   ----------

rfq_vendor_first_field = "//td[contains(., 'Autotest User')]"
rfq_vendor_name_id = "rfq-vendor-name"
rfq_vendor_search_id = "rfq-vendor-search"
rfq_pn_aval_id = "rfq-pn-aval"
rfq_pn_salestype_id = "rfq-pn-salestype"
rfq_pn_description_id = "rfq-pn-description"
rfq_pn_rate_id = "rfq-pn-rate"
rfq_qty_avail_id = "rfq-pn-aqty"
rfq_pn_uom_id = "rfq-pn-uom"
rfq_pn_condition_id = "rfq-pn-condition"
rfq_pn_condition = "//li[contains(., 'FN')]"
rfq_pn_location_id = "rfq-pn-location"
rfq_pn_tags_id = "rfq-tags"
rfq_tag_date_id = "rfq-tag-date"
rfq_cert_type_id = "rfq-cert-type"
rfq_trace_id = "rfq-trace"
rfq_warranty_id = "rfq-warranty"
rfq_shop_id = "rfq-shop"
rfq_sn_id = "rfq-sn"
rfq_pn_cert = "//li[contains(., 'CofC Only')]"
rfq_create_new_line = "//button[contains(., 'Create new line')]"
vrq_accept_id = "rfq-button-accept-description"

#   ----------  Verify Requested Part  ----------

recommended_description_id = "rfq-radio-recommended-description"
stored_description_id = "rfq-radio-stored-description-1"
current_description_id = "rfq-radio-current-description"
vrp_cancel_id = "rfq-button-cancel-description"

#   ----------  Stock Outright  ----------

rfq_stock_outright = "//li[contains(., 'Stock Outright')]"

so_stock_unit_cost_id = "rfq-stock-unit-cost"
so_unit_price_id = "rfq-stock-unit-price"
so_vendor_moq_id = "rfq-stock-vendor-moq"
so_stock_moq_id = "rfq-stock-moq"
so_min_vendor_order_id = "rfq-stock-min-vendor-order"
so_stock_qty_id = "rfq-stock-qty"
so_stock_total_cost_id = "rfq-stock-total-cost"
so_stock_total_price_id = "rfq-stock-total-price"
so_lead_time_id = "rfq-stock-lead-time"
so_mgm_id = "rfq-stock-pl-mgm"
so_mgm_percent_id = "rfq-stock-mgm-percent"

#   ----------  Exchange  ----------

rfq_exchange = "//li[contains(., 'Exchange')]"

ex_fee_cost_id = "rfq-exchange-fee-cost"
ex_fee_price_id = "rfq-exchange-fee-price"
ex_ber_cost_id = "rfq-exchange-ber-cost"
ex_ber_price_id = "rfq-exchange-ber-price"
ex_vendor_rtrn_days_id = "rfq-exchange-rtrn-day"
ex_cust_rtrn_price_id="rfq-exchange-rtrn-priceday"
ex_lead_time_id = "rfq-exchange-lead-time"
ex_delivery_time_id = "rfq-exchange-delivery-time"
ex_service_cost_id = "rfq-exchange-service-cost"
ex_service_price_id = "rfq-exchange-service-price"
ex_qty_id = "rfq-exchange-qty"
ex_cost_total_id = "rfq-exchange-total-cost"
ex_total_price_id = "rfq-exchange-total-price"
ex_mgm_id = "rfq-exchange-mgm"
ex_mgm_percent_id = "rfq-exchange-mgm-percent"

#   ----------  Repair  ----------

rfq_repair = "//li[contains(., 'Repair/OH')]"

repair_b_check_cost_id = "rfq-repair-bcost"
repair_b_check_price_id = "rfq-repair-bprice"
repair_lead_b_check_id = "rfq-repair-bcheck"
repair_delivery_b_check_id = "rfq-repair-bcheck-price"
repair_avg_repair_cost_id = "rfq-repair-avg-cost"
repair_avg_repair_price_id = "rfq-repair-avg-price"
repair_lead_time_id = "rfq-repair-lead-time"
repair_delivery_time_id = "rfq-repair-delivery-time"
repair_max_cost_id = "rfq-repair-max-cost"
repair_max_price_id = "rfq-repair-max-price"
repair_mgm_id = "rfq-repair-mgm-price"
repair_mgm_percent_id = "rfq-repair-mgm-percent"

#   ----------  Basic Information   ----------

rfq_ic_id = "rfq-ichg"
rfq_notes_id = "rfq-notes"
rfq_non_printed_notes_id = "rfq-np-notes"
rfq_v_quote_id = "rfq-vquote"
rfq_v_date_id = "rfq-vqdate"

territory = "//li[contains(., 'US')]"

rfq_save_button_id = "rfq-save-buttons"
rfq_save_and_continue_id = "rfq-save-button-0"
rfq_save_and_quote_id = "rfq-save-button-1"
rfq_save_and_new_id = "rfq-save-button-2"
rfq_save_and_exit_id = "rfq-save-button-3"

create_new_quote_button = "//button[contains(.,'Create New')]"
created_quotes_header = "//div[contains(., 'Created quotes')]"

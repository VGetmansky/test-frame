material_arrival_id = "menubar_item_WHStock"
shipping_notice_id = "menubar_item_WHStock_Notice"
inspection_id = "menubar_item_WHStock_Inspection"
receiving_id = "menubar_item_WHStock_Receiving"
packing_id = "menubar_item_WHStock_Packing"
cargo_sign_off_form_id = "menubar_item_WHStock_Shipping"

#   material_arrival_expected_url = "index.php?module=WHStock&view=Income"
ma_test_url = "http://crmqa.bai-inc.eu/crmqa/#/shipping/arrival"
ma_test_history_url = "http://crmqa.bai-inc.eu/crmqa/#/shipping/arrival/history"
material_arrival_expected_url = "crm/#/shipping/arrival"
shipping_notice_expected_url = "index.php?module=WHStock&view=Notice"
inspection_expected_url = "index.php?module=WHStock&view=Inspection"
receiving_expected_url = "index.php?module=WHStock&view=Receiving"
packing_expected_url = "index.php?module=WHStock&view=Packing"
cargo_sign_off_expected_url = "index.php?module=WHStock&view=Shipping"

awb_check_id = "awb_check_label"
type_awb_id = "awb_input"
vendor_check_id = "vendor_check_label"

# vendor_select_id = "vendor_select_chzn"

#   ----------  Material arrival    ----------

ma_arrived_0_id = "arrival-arrived-0-0"
ma_arrived_note_0_id = "arrival-note-0-0"
ma_arrived_1_id = "arrival-arrived-0-1"
ma_arrived_note_1_id = "arrival-note-0-1"
ma_arrived_2_id = "arrival-arrived-0-2"
ma_arrived_note_2_id = "arrival-note-0-2"

ma_arrival_history_button_id = "arrival-history"
ma_arrival_deliver_id = "arrival-deliver"


#   ----------  Arrival History    ----------


ah_inspection_id = "arrival-history-inspection"
ah_notice_id = "arrival-history-notice"

vendor_select_id = "arrival-history-vendor"
# vendor_select_id = "arrival-so"
po_select_id = "arrival-po"
po_filter_id = "po_filter"
so_filter_id = "so_filter"
material_arrival_checkboxes = '//div[@class="checkbox po-line-item-checkbox"]'
deliver_button = '//div[contains(.,"Deliver")]'
clear_button = '//div[contains(.,"Clear")]'
cancel_button = '//div[contains(.,"Cancel")]'
notes_id = "notes"

select_account_id = "account_select_chzn"
notice_id = "notes"
critical_status_id = "critical"
urgent_status_id = "urgent"
routine_status_id = "rountine"
on_or_by_id = "on_or_by"

inspection_select_id = "inspection_select_chzn"
select_all_button_id = "select_all_label"
deselact_all_button_id = "deselect_all_label"
material_arrival_inspection_checkboxes = '//div[@class="whstc-checkbox-label inspected-label"]'

autotest_vendor = '//li[contains(., "Autotest User")]'
autotest_account = '//li[contains(., "Account for autotests")]'

isle_id = "bin_isle_1"
shelf_id = "bin_shelf_1"
holder_id = "bin_holder_1"

# deliver_button = '//div[contains(., "Deliver")]'
deliver_button_id = "arrival-deliver"
send_notice_button = '//div[contains(., "Send Notice")]'
approve_button = '//div[contains(., "Approve")]'
receive_button = '//div[contains(., "Receive")]'

ma_checkbox = '//span[@class="el-checkbox__inner"]'

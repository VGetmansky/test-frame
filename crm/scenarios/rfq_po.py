import pytest
from crm.tests import login_tests
from crm.tests import rfq_tests
from crm.tests import quotest_tests
from crm.tests import so_tests
from crm.tests import invoice_tests
from crm.tests import po_tests
from crm.tests import addnewentity_tests
from crm.data import rfq_to_po_data


@pytest.allure.testcase('login')
@pytest.mark.test
class TestLogInApp:
    def test_open_url(self, driver, url):
        with pytest.allure.step('Open URL'):
                login_tests.open_url(driver, url)

    def test_add_credentials(self, driver, username, password):
        with pytest.allure.step('Add cridentials'):
            login_tests.add_credentials(driver, username, password)

    def test_submit_form(self, driver):
        with pytest.allure.step('Submit Form'):
            login_tests.submit_form(driver)

    def test_verify_url(self, driver, url):
        with pytest.allure.step('Verify URL'):
            login_tests.verify_url(driver, url)


@pytest.allure.testcase('Work With RFQ')
@pytest.mark.test
class TestWorkWithRFQList:
    def test_open_rfq_tab(self, driver):
        with pytest.allure.step('Select RFQ'):
            rfq_tests.select_rfq(driver)


@pytest.mark.test
class TestClickAddButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add RFQ'):
            rfq_tests.click_add_rfq(driver, url)


@pytest.mark.test
class TestCreateRfq:

    def test_select_vendor(self, driver):
        with pytest.allure.step('Fill vendor field'):
            rfq_tests.fill_in_vendor_field(driver)

    def test_priority(self, driver):
        with pytest.allure.step('Select priority'):
            rfq_tests.select_priority(driver)

    def test_select_account(self, driver):
        with pytest.allure.step('Fill account'):
            rfq_tests.fill_in_account_field(driver)

    def test_select_contact(self, driver):
        with pytest.allure.step('Contact field'):
            rfq_tests.fill_in_contact_field(driver)

    def test_fill_customer_quote(self, driver):
        with pytest.allure.step('Fill customer quote'):
            rfq_tests.fill_in_customer_quote(driver)

    def test_fill_received_via(self, driver):
        with pytest.allure.step('Fill recieved via'):
            rfq_tests.fill_in_received_via(driver)

    def test_select_sale_terms(self, driver):
        with pytest.allure.step('Select sale terms'):
            rfq_tests.select_sale_terms(driver)

    def test_delivery_terms(self, driver):
        with pytest.allure.step('Select sale terms'):
            rfq_tests.select_sale_terms(driver)

    def test_delivery_terms_test_field(self, driver):
        with pytest.allure.step('Fill delivery terms'):
            rfq_tests.fill_in_delivery_terms_text_field(driver)

    def test_fill_description(self, driver):
        with pytest.allure.step('Fill description'):
            rfq_tests.fill_in_description(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select territory'):
            rfq_tests.select_territory(driver)

    def test_select_aircraft(self, driver):
        with pytest.allure.step('Fill aircraft'):
            rfq_tests.fill_in_aircraft_field(driver)

    def test_select_location(self, driver):
        with pytest.allure.step('Fill contact'):
            rfq_tests.fill_in_contact_field(driver)

    def test_select_pl_status(self, driver):
        with pytest.allure.step('Select pl status'):
            rfq_tests.select_pl_status(driver)

    def test_add_part_line(self, driver):
        with pytest.allure.step('Click Add part number'):
            rfq_tests.click_add_part_number(driver)

    def test_fill_part_number(self, driver):
        with pytest.allure.step('Fill part number name'):
            rfq_tests.fill_part_number_name(driver)

    def test_fill_pn_qty(self, driver):
        with pytest.allure.step('Fill pn qty'):
            rfq_tests.fill_pn_qty(driver)

    def test_click_insert_pn(self, driver):
        with pytest.allure.step('Click insert pn'):
            rfq_tests.click_insert_pn(driver)

    def test_fill_pn_vendor(self, driver):
        with pytest.allure.step('Fill PN Vendor'):
            rfq_tests.fill_in_vendor(driver)

    def test_fill_pn_description(self, driver):
        with pytest.allure.step('Fill PN Description'):
            rfq_tests.fill_in_pn_description(driver)

# Stock Outright
    def test_click_offer(self, driver):
        with pytest.allure.step('Click offer'):
            rfq_tests.click_offer(driver)

    def test_fill_unit_cost(self, driver):
        with pytest.allure.step('Fill unit cost'):
            rfq_tests.fill_in_unit_cost(driver)

    def test_fill_unit_price(self, driver):
        with pytest.allure.step('Fill unit price'):
            rfq_tests.fill_in_unit_price(driver)

    def test_fill_vendor_moq(self, driver):
        with pytest.allure.step('Fill vendor moq'):
            rfq_tests.fill_in_vendor_moq(driver)

    def test_fill_moq(self, driver):
        with pytest.allure.step('Fill moq'):
            rfq_tests.fill_in_moq(driver)

    def test_fill_stock_outright_lead_time(self, driver):
        with pytest.allure.step('Fill stock outright lead time'):
            rfq_tests.fill_in_stock_outright_lead_time(driver)

    def test_fill_stock_outright_delivery_time(self, driver):
        with pytest.allure.step('Fill stock outright delivery time'):
            rfq_tests.fill_in_stock_outright_delivery_time(driver)

    # def test_fill_min_vendor_order(self, driver):
    #     tests.fill_in_min_vendor_order(driver)

# Exchange
    def test_click_alt_offer_exchange(self, driver):
        with pytest.allure.step('Click alt offer'):
            rfq_tests.click_alt_offer(driver)

    def test_select_sales_type(self, driver):
        with pytest.allure.step('Select exchange type'):
            rfq_tests.select_exchange_type(driver)

    def test_fill_ex_fee_cost(self, driver):
        with pytest.allure.step('Fill exchange fee cost'):
            rfq_tests.fill_in_exchange_fee_cost(driver)

    def test_fill_vendor_rtnr_days(self, driver):
        with pytest.allure.step('Fill exchange vendor rtrn days'):
            rfq_tests.fill_in_exchange_vendor_rtrn_days(driver)

    def test_fill_exchange_service_cost(self, driver):
        with pytest.allure.step('Fill exchange service cost'):
            rfq_tests.fill_in_exchange_service_cost(driver)

    def test_fill_exchange_ber_cost(self, driver):
        with pytest.allure.step('Fill exchange ber cost'):
            rfq_tests.fill_in_exchange_ber_cost(driver)

    def test_fill_exchange_lead_time(self, driver):
        with pytest.allure.step('Fill exchange lead time'):
            rfq_tests.fill_in_exchange_lead_time(driver)

    def test_fill_exchange_cost_total(self, driver):
        with pytest.allure.step('Fill exchange cost total'):
            rfq_tests.fill_in_exchange_cost_total(driver)

    def test_fill_exchange_qty(self, driver):
        with pytest.allure.step('Fill exchange qty'):
            rfq_tests.fill_in_exchange_qty(driver)

    def test_fill_ex_fee_price(self, driver):
        with pytest.allure.step('Fill exchange fee price'):
            rfq_tests.fill_in_exchange_fee_price(driver)

    def test_fill_exchange_cust_rtrn_days(self, driver):
        with pytest.allure.step('Fill exchange cust rtrn days'):
            rfq_tests.fill_in_exchange_cust_rtrn_days(driver)

    def test_fill_exchange_service_prive(self, driver):
        with pytest.allure.step('Fill exchange service price'):
            rfq_tests.fill_in_exchange_service_price(driver)

    def test_fill_exchange_ber_price(self, driver):
        with pytest.allure.step('Fill exhange ber price'):
            rfq_tests.fill_in_exchange_ber_price(driver)

    def test_fill_exchange_delivery_time(self, driver):
        with pytest.allure.step('Fill exchange delivery time'):
            rfq_tests.fill_in_exchange_delivery_time(driver)

# Repair
    def test_click_alt_offer_repair(self, driver):
        with pytest.allure.step('Click alt offer'):
            rfq_tests.click_alt_offer(driver)

    def test_select_repair(self, driver):
        with pytest.allure.step('Select repair type'):
            rfq_tests.select_repair_type(driver)

    def test_fill_bcheck_price(self, driver):
        with pytest.allure.step('Fill repair bcheck cost'):
            rfq_tests.fill_in_repair_bcheck_cost(driver)

    def test_fill_lead_bcheck(self, driver):
        with pytest.allure.step('Fill repair lead b check'):
            rfq_tests.fill_in_repair_lead_b_check(driver)

    def test_fill_avg_repair_cost(self, driver):
        with pytest.allure.step('Fill avg repair price'):
            rfq_tests.fill_in_avg_repair_price(driver)

    def test_fill_max_repair_cost(self, driver):
        with pytest.allure.step('Fill max repair cost'):
            rfq_tests.fill_in_max_repair_cost(driver)

    def test_fill_repair_lead_time(self, driver):
        with pytest.allure.step('Fill repair lead time'):
            rfq_tests.fill_in_repair_lead_time(driver)

    def test_fill_repair_qty(self, driver):
        with pytest.allure.step('Fill repair qty'):
            rfq_tests.fill_in_repair_qty(driver)

    def test_repair_bcheck_price(self, driver):
        with pytest.allure.step('Fill repair bcheck price'):
            rfq_tests.fill_in_repair_bcheck_price(driver)

    def test_fill_delivery_bcheck(self, driver):
        with pytest.allure.step('Fill repair delivery b check'):
            rfq_tests.fill_in_repair_delivery_b_check(driver)

    def test_fill_avg_repair_price(self, driver):
        with pytest.allure.step('Fill avg repair price'):
            rfq_tests.fill_in_avg_repair_price(driver)

    def test_fill_max_repair_price(self, driver):
        with pytest.allure.step('Fill max repair price'):
            rfq_tests.fill_in_max_repair_price(driver)

    def test_fill_repair_delivery_time(self, driver):
        with pytest.allure.step('Fill repair delivery time'):
            rfq_tests.fill_in_repair_delivery_time(driver)

    def test_click_save_rfq(self, driver):
        with pytest.allure.step('Click save rfq'):
            rfq_tests.click_save_rfq(driver)


@pytest.mark.test
class TestClickAddQuoteButton:
    def test_click_add_quote_button(self, driver, url):
        with pytest.allure.step('Click add Quote'):
            addnewentity_tests.test_click_add_quote_from_rfq(driver)


@pytest.mark.test
class TestCreateQuote:

    # def test_select_account(self, driver):
    #     with pytest.allure.step('Fill Account'):
    #         quotest_tests.fill_in_account_field(driver)

    def test_fill_in_cust_ref(self, driver):
        with pytest.allure.step('Fill cust ref'):
            quotest_tests.fill_in_cust_ref(driver)

    def test_fill_in_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            quotest_tests.fill_in_billing_address(driver)

    def test_fill_in_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            quotest_tests.fill_in_shipping_address(driver)

    def test_fill_in_place_of_delivery(self, driver):
        with pytest.allure.step('Fill place of delivery'):
            quotest_tests.fill_in_place_of_delivery(driver)

    def test_select_quote_status(self,driver):
        with pytest.allure.step('Select quote status'):
            quotest_tests.select_quote_status(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            quotest_tests.select_proirity(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select terms of delivery'):
            quotest_tests.select_terms_of_delivery(driver)

    def test_select_terms_of_sale(self, driver):
        with pytest.allure.step('Select terms sale'):
            quotest_tests.select_terms_sale(driver)



    # def test_add_product(self, driver):
    #     with pytest.allure.step('Add product'):
    #         quotest_tests.add_product(driver)



    # def test_close_alert(self, driver):
    #     tests.close_alert(driver)

    def test_fill_in_billing_po_box(self, driver):
        with pytest.allure.step('Fill billing box'):
            quotest_tests.fill_in_billing_po_box(driver)

    def test_fill_in_billing_city(self, driver):
        with pytest.allure.step('Fill billing city'):
            quotest_tests.fill_in_billing_city(driver)

    def test_fill_in_billing_state(self, driver):
        with pytest.allure.step('Fill billing state'):
            quotest_tests.fill_in_billing_state(driver)

    def test_fill_in_billing_post_code(self, driver):
        with pytest.allure.step('Fill billing post code'):
            quotest_tests.fill_in_billing_post_code(driver)

    def test_fill_in_billing_post_country(self, driver):
        with pytest.allure.step('Fill billing country'):
            quotest_tests.fill_in_billing_country(driver)

    def test_fill_in_shipping_po_box(self, driver):
        with pytest.allure.step('Fill shipping box'):
            quotest_tests.fill_in_shipping_po_box(driver)

    def test_fill_in_shipping_city(self, driver):
        with pytest.allure.step('Fill shipping city'):
            quotest_tests.fill_in_shipping_city(driver)

    def test_fill_in_shipping_state(self, driver):
        with pytest.allure.step('Fill shipping state'):
            quotest_tests.fill_in_shipping_state(driver)

    def test_fill_in_shipping_post_code(self, driver):
        with pytest.allure.step('Fill shipping post code'):
            quotest_tests.fill_in_shipping_post_code(driver)

    def test_fill_in_shipping_post_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            quotest_tests.fill_in_shipping_country(driver)

    def test_fill_in_description_details(self, driver):
        with pytest.allure.step('Fill description details'):
            quotest_tests.fill_in_description_details(driver)

    def test_save_so(self, driver):
        with pytest.allure.step('Save SO'):
            quotest_tests.save_so(driver)


@pytest.mark.test
class TestClickAddSoButton:
    def test_click_add_quote_button(self, driver, url):
        with pytest.allure.step('Click add SO'):
            addnewentity_tests.test_click_add_so_from_quote(driver)


@pytest.mark.test
class TestCreateSO:

    def test_fill_in_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            so_tests.fill_in_billing_address(driver)

    def test_fill_in_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            so_tests.fill_in_shipping_address(driver)

    # def test_select_account(self, driver):
    #     with pytest.allure.step('Fill account field'):
    #         so_tests.fill_in_account_field(driver)

    # def test_add_product(self, driver):
    #     with pytest.allure.step('Add product'):
    #         so_tests.add_product(driver)

    def test_fill_in_client_po(self, driver):
        with pytest.allure.step('Fill client PO'):
            so_tests.fill_in_client_po(driver)

    def test_fill_in_billing_po_box(self, driver):
        with pytest.allure.step('Fill billing po box'):
            so_tests.fill_in_billing_po_box(driver)

    def test_fill_in_billing_city(self, driver):
        with pytest.allure.step('Fill billing city'):
            so_tests.fill_in_billing_city(driver)

    def test_fill_in_billing_state(self, driver):
        with pytest.allure.step('Fill billing state'):
            so_tests.fill_in_billing_state(driver)

    def test_fill_in_billing_post_code(self, driver):
        with pytest.allure.step('Fill billing post code'):
            so_tests.fill_in_billing_post_code(driver)

    def test_fill_in_billing_post_country(self, driver):
        with pytest.allure.step('Fill billing country'):
            so_tests.fill_in_billing_country(driver)

    def test_fill_in_shipping_po_box(self, driver):
        with pytest.allure.step('Fill shipping po box'):
            so_tests.fill_in_shipping_po_box(driver)

    def test_fill_in_shipping_city(self, driver):
        with pytest.allure.step('Fill shipping city'):
            so_tests.fill_in_shipping_city(driver)

    def test_fill_in_shipping_state(self, driver):
        with pytest.allure.step('Fill shipping state'):
            so_tests.fill_in_shipping_state(driver)

    def test_fill_in_shipping_post_code(self, driver):
        with pytest.allure.step('Fill shipping post code'):
            so_tests.fill_in_shipping_post_code(driver)

    def test_fill_in_shipping_post_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            so_tests.fill_in_shipping_country(driver)

    def test_save_so(self, driver):
        with pytest.allure.step('Save SO'):
            so_tests.save_so(driver)


@pytest.mark.test
class TestClickAddPoButton:
    def test_click_add_po_button(self, driver, url):
        with pytest.allure.step('Click add PO'):
            addnewentity_tests.test_click_add_po_from_so(driver)


@pytest.mark.test
class TestClickEditPO:
    def test_click_open_po_button(self, driver, url):
        with pytest.allure.step('Open PO'):
            addnewentity_tests.click_open_po(driver, url)

    def test_edit_po_profile(self, driver):
        with pytest.allure.step('edit PO'):
            po_tests.click_edit_po(driver, rfq_to_po_data.edit_po_profile_id)


@pytest.mark.test
class TestCreatePO:

    # def test_select_vendor(self, driver):
    #     with pytest.allure.step('Select Vendor'):
    #         po_tests.select_vendor(driver)

    def test_copy_vendor_address(self, driver):
        with pytest.allure.step('Copy Vendor Address'):
            po_tests.copy_vendor_address(driver)

    def test_copy_company_address(self, driver):
        with pytest.allure.step('Copy Company Address'):
            po_tests.copy_company_address(driver)

    def test_fill_vendor_po(self, driver):
        with pytest.allure.step('Fill Vendor PO'):
            po_tests.fill_in_vendor_po(driver)

    def test_fill_tracking_number(self, driver):
        with pytest.allure.step('Fill tracking number'):
            po_tests.fill_in_tracking_number(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            po_tests.select_priority(driver)

    # def test_fill_account(self, driver):
    #     with pytest.allure.step('Fill account'):
    #         po_tests.fill_in_account(driver)

    # def test_select_status(self, driver):
    #     with pytest.allure.step('Select Status'):
    #         po_tests.select_status(driver)

    def test_select_terms_of_payment(self, driver):
        with pytest.allure.step('select terms of payment'):
            po_tests.select_terms_of_payment(driver)

    def test_fill_delivery_place(self, driver):
        with pytest.allure.step('Fill delivery place'):
            po_tests.fill_in_delivery_place(driver)

    def test_select_due_date(self, driver):
        with pytest.allure.step('Due date'):
            po_tests.select_due_date(driver)

    def test_select_aircraft(self, driver):
        with pytest.allure.step('Aircraft'):
            po_tests.select_aircraft(driver)

    def test_fill_po_number(self, driver):
        with pytest.allure.step('fill po number'):
            po_tests.fill_in_po_number(driver)

    def test_fill_requisition_number(self, driver):
        with pytest.allure.step('Fill requisition number'):
            po_tests.fill_in_requisition_number(driver)

    def test_select_contact_name(self, driver):
        with pytest.allure.step('Select contact name'):
            po_tests.select_contact_name(driver)

    def test_select_ship_via(self, driver):
        with pytest.allure.step('Select ship via'):
            po_tests.select_ship_via(driver)

    def test_fill_sales_commission(self, driver):
        with pytest.allure.step('Fill sales commission'):
            po_tests.fill_in_sales_commission(driver)

    def test_excise_duty(self, driver):
        with pytest.allure.step('Fill excise duty'):
            po_tests.fill_in_excise_duty(driver)

        # def test_select_assigned_to(self, driver):
        #     tests.select_assigned_to(driver)

    def test_select_terms_of_delivery(self, driver):
         with pytest.allure.step('Select terms of delivery'):
            po_tests.select_terms_of_delivery(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('select territory'):
            po_tests.select_territory(driver)

    def test_select_location(self, driver):
        with pytest.allure.step('select location'):
            po_tests.select_location(driver)

    def test_fill_vendor_po_box(self, driver):
        with pytest.allure.step('Fill vendor po box'):
            po_tests.fill_in_vendor_po_box(driver)

    def test_fill_vendor_city(self, driver):
        with pytest.allure.step('Fill vendor city'):
            po_tests.fill_in_vendor_city(driver)

    def test_fill_vendor_state(self, driver):
        with pytest.allure.step('fill vendor state'):
            po_tests.fill_in_vendor_state(driver)

    def test_fill_vendor_post_code(self, driver):
        with pytest.allure.step('Fill vendor post code'):
            po_tests.fill_in_vendor_post_code(driver)

    def test_fill_vendor_country(self, driver):
        with pytest.allure.step('dill vendor country'):
            po_tests.fill_in_vendor_country(driver)

    def test_fill_shipping_po_box(self, driver):
        with pytest.allure.step('fill shipping po box'):
            po_tests.fill_in_shipping_po_box(driver)

    def test_fill_shipping_city(self, driver):
        with pytest.allure.step('fill shipping city'):
            po_tests.fill_in_shipping_city(driver)

    def test_fill_shipping_state(self, driver):
        with pytest.allure.step('fill shipping state'):
            po_tests.fill_in_shipping_state(driver)

    def test_fill_shipping_post_code(self, driver):
        with pytest.allure.step('fill shipping post code'):
            po_tests.fill_in_shipping_post_code(driver)

    def test_fill_shipping_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            po_tests.fill_in_shipping_country(driver)

        # def test_fill_description(self, driver):
        #     tests.fill_in_description(driver)

    def test_add_product(self, driver):
        with pytest.allure.step('Add product'):
            po_tests.add_product(driver)

    def test_save_po(self, driver):
        with pytest.allure.step('save PO'):
            po_tests.save_po(driver)


@pytest.mark.test
class TestOpSOList:
    def test_open_so_tab(self, driver):
        with pytest.allure.step('Select SO'):
            so_tests.select_sales_orders(driver)


@pytest.mark.test
class TestOpenSODetails:
    def test_open_so_details(self, driver, url):
        with pytest.allure.step('Open SO details'):
            invoice_tests.open_so_details(driver, url)


@pytest.allure.testcase('Work With Quotes')
@pytest.mark.test
class TestCreateInvoice:

    def test_click_add_invoice(self, driver):
        with pytest.allure.step('Click add invoice'):
            invoice_tests.click_add_invoice(driver)

    def test_fill_invoice_no(self, driver):
        with pytest.allure.step('Fill invoice no'):
            invoice_tests.fill_in_invoice_no(driver)

    def test_fill_customer_po(self, driver):
        with pytest.allure.step('Fill customer PO'):
            invoice_tests.fill_in_customer_po(driver)

    def test_fill_customer_no(self, driver):
        with pytest.allure.step('Fill customer no'):
            invoice_tests.fill_in_customer_no(driver)

    def test_select_terms_of_sale(self, driver):
        with pytest.allure.step('Select terms of sale'):
            invoice_tests.select_terms_of_sale(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select terms of delivery'):
            invoice_tests.select_terms_of_delivery(driver)

    def test_fill_sales_commission(self, driver):
        with pytest.allure.step('Fill sales commission'):
            invoice_tests.fill_in_sales_commision(driver)

    def test_fill_account(self, driver):
        with pytest.allure.step('Fill account'):
            invoice_tests.fill_in_account(driver)

    def test_fill_boxes(self, driver):
        with pytest.allure.step('Fill boxes'):
            invoice_tests.fill_in_boxes(driver)

    def test_fill_dimensions(self, driver):
        with pytest.allure.step('Fill dimensions'):
            invoice_tests.fill_in_dimensions(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select territory'):
            invoice_tests.select_territory(driver)

    def test_select_due_date(self, driver):
        with pytest.allure.step('Select due date'):
            invoice_tests.select_due_date(driver)

    def test_select_status(self, driver):
        with pytest.allure.step('Select status'):
            invoice_tests.select_status(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            invoice_tests.select_priority(driver)

    def test_fill_place_of_delivery(self, driver):
        with pytest.allure.step('Fill place of delivery'):
            invoice_tests.fill_in_place_of_delivery(driver)

    def test_select_ship_via(self, driver):
        with pytest.allure.step('Select ship via'):
            invoice_tests.select_ship_via(driver)

    def test_fill_awb(self, driver):
        with pytest.allure.step('Fill awb'):
            invoice_tests.fill_in_awb(driver)

    def test_fill_weight(self, driver):
        with pytest.allure.step('Fill weight'):
            invoice_tests.fill_in_weight(driver)

    def test_fill_invoice_date(self, driver):
        with pytest.allure.step('Select invoice date'):
            invoice_tests.select_invoice_date(driver)

    def test_fill_order_date(self, driver):
        with pytest.allure.step('Select order date'):
            invoice_tests.select_order_date(driver)

    # def test_fill_total_payments(self, driver):
    #    with pytest.allure.step('Fill total payments'):
    #        invoice_tests.fill_in_total_payments(driver)

    #def test_fill_percent_paid(self, driver):
    #   with pytest.allure.step('Fill percent paid'):
    #      invoice_tests.fill_in_percent_paid(driver)

    def test_fill_special_notes(self, driver):
        with pytest.allure.step('Fill special note'):
            invoice_tests.fill_in_special_note(driver)

    def test_click_save_button(self, driver):
        with pytest.allure.step('Click save invoice button'):
            invoice_tests.click_save_button(driver)

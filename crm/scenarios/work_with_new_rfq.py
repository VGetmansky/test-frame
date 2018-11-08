import pytest
from crm.tests import new_rfq_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With RFQ')
@pytest.mark.test
class TestWorkWithRFQList:
    def test_open_rfq_tab(self, driver):
        with pytest.allure.step('Select RFQ'):
            tests.select_rfq(driver)


# @pytest.mark.test
class TestRFQList:
    def test_filter_list_by_creator(self, driver):
        with pytest.allure.step('Filter by creator'):
            tests.filter_by_creator(driver)


@pytest.mark.test
class TestClickAddButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add RFQ'):
            tests.click_add_rfq(driver, url)


@pytest.mark.test
class TestCreateRfq:

    def test_select_account(self, driver):
        with pytest.allure.step('Fill account'):
            tests.fill_in_account_field(driver)

    def test_select_contact(self, driver):
        with pytest.allure.step('Contact field'):
            tests.fill_in_contact_field(driver)

    def test_fill_customer_quote(self, driver):
        with pytest.allure.step('Fill customer quote'):
            tests.fill_in_customer_quote(driver)

    def test_fill_received_via(self, driver):
        with pytest.allure.step('Fill recieved via'):
            tests.fill_in_received_via(driver)

    def test_fill_description(self, driver):
        with pytest.allure.step('Fill description'):
            tests.fill_in_description(driver)

    def test_fill_place_of_delivery(self, driver):
        with pytest.allure.step('Fill place of delivery'):
            tests.fill_in_place_of_delivery(driver)

    def test_select_sale_terms(self, driver, url):
        with pytest.allure.step('Select sale terms'):
            tests.select_sale_terms(driver, url)

    def test_delivery_terms(self, driver):
        with pytest.allure.step('Select sale terms'):
            tests.select_delivery_terms(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select territory'):
            tests.select_territory(driver)

    def test_priority(self, driver):
        with pytest.allure.step('Select priority'):
            tests.select_priority(driver)

    def test_select_assigned_to(self, driver):
        with pytest.allure.step('Select Assigned To'):
            tests.select_assigned_to(driver)

    def test_fill_part_number(self, driver):
        with pytest.allure.step('Fill part number name'):
             tests.fill_part_number_name(driver)

#   WA checkbox Cannot scroll into view
#     def test_uncheck_will_advice(self, driver):
#         with pytest.allure.step('Uncheck Will Advice'):
#             tests.uncheck_will_advice(driver)

# сменились поля на дропдаун
    # def test_select_aircraft(self, driver):
    #     with pytest.allure.step('Fill aircraft'):
    #         tests.fill_in_aircraft_field(driver)
    #
    # def test_select_location(self, driver):
    #     with pytest.allure.step('Fill contact'):
    #         tests.fill_in_contact_field(driver)

    def test_fill_pn_description(self, driver):
        with pytest.allure.step('Fill PN Description'):
            tests.fill_in_pn_description(driver)

    def test_select_vendor(self, driver):
        with pytest.allure.step('Fill vendor field'):
            tests.fill_in_vendor_field(driver)

    def test_fill_pn_qty(self, driver):
        with pytest.allure.step('Fill Stock Outright Aval.Qty'):
            tests.fill_in_pli_aval_qty(driver)

    def test_select_location(self, driver):
        with pytest.allure.step('Fill contact'):
            tests.fill_in_pli_location(driver)

    def test_select_rate(self, driver):
        with pytest.allure.step('Fill contact'):
            tests.fill_in_pli_rate(driver)

#     def test_select_pl_status(self, driver):
#         with pytest.allure.step('Select pl status'):
#             tests.select_pl_status(driver)
#
#     def test_add_part_line(self, driver):
#         with pytest.allure.step('Click Add part number'):
#             tests.click_add_part_number(driver)
#
#     def test_fill_pn_qty(self, driver):
#         with pytest.allure.step('Fill pn qty'):
#             tests.fill_pn_qty(driver)
#
#     def test_click_insert_pn(self, driver):
#         with pytest.allure.step('Click insert pn'):
#             tests.click_insert_pn(driver)
#
#     def test_fill_pn_vendor(self, driver):
#         with pytest.allure.step('Fill PN Vendor'):
#             tests.fill_in_vendor(driver)
#
#
#     def test_fill_stock_outright_plli_aval_qty(self, driver):
#         with pytest.allure.step('Fill Stock Outright Aval.Qty'):
#             tests.fill_in_plli_aval_qty(driver)
#
# # Stock Outright
#     def test_click_offer(self, driver):
#         with pytest.allure.step('Click offer'):
#             tests.click_offer(driver)

    def test_fill_unit_cost(self, driver):
        with pytest.allure.step('Fill unit cost'):
            tests.fill_in_unit_cost(driver)

    def test_fill_unit_price(self, driver):
        with pytest.allure.step('Fill unit price'):
            tests.fill_in_unit_price(driver)

    def test_fill_vendor_moq(self, driver):
        with pytest.allure.step('Fill vendor moq'):
            tests.fill_in_vendor_moq(driver)

    def test_fill_moq(self, driver):
        with pytest.allure.step('Fill moq'):
            tests.fill_in_moq(driver)
#
#     def test_fill_stock_outright_lead_time(self, driver):
#         with pytest.allure.step('Fill stock outright lead time'):
#             tests.fill_in_stock_outright_lead_time(driver)
#
#     def test_fill_stock_outright_delivery_time(self, driver):
#         with pytest.allure.step('Fill stock outright delivery time'):
#             tests.fill_in_stock_outright_delivery_time(driver)

    # def test_fill_min_vendor_order(self, driver):
    #     with pytest.allure.step('Fill stock outright Min Ven order'):
    #         tests.fill_in_min_vendor_order(driver)

    def test_fill_stock_outright_notes(self, driver):
        with pytest.allure.step('Fill stock outright notes'):
            tests.fill_note(driver)

    def test_fill_stock_outright_non_print_notes(self, driver):
        with pytest.allure.step('Fill stock outright non-printed notes'):
            tests.fill_non_printed_note(driver)

    def test_fill_stock_outright_vquotes(self, driver):
        with pytest.allure.step('Fill V.Quote'):
            tests.fill_v_quote(driver)
#
# # Exchange
#     def test_click_alt_offer_exchange(self, driver):
#         with pytest.allure.step('Click alt offer'):
#             tests.click_alt_offer(driver)
#
#     def test_select_sales_type(self, driver):
#         with pytest.allure.step('Select exchange type'):
#             tests.select_exchange_type(driver)
#
#     def test_fill_ex_fee_cost(self, driver):
#         with pytest.allure.step('Fill exchange fee cost'):
#             tests.fill_in_exchange_fee_cost(driver)
#
#     def test_fill_vendor_rtnr_days(self, driver):
#         with pytest.allure.step('Fill exchange vendor rtrn days'):
#             tests.fill_in_exchange_vendor_rtrn_days(driver)
#
#     def test_fill_exchange_service_cost(self, driver):
#         with pytest.allure.step('Fill exchange service cost'):
#             tests.fill_in_exchange_service_cost(driver)
#
#     def test_fill_exchange_ber_cost(self, driver):
#         with pytest.allure.step('Fill exchange ber cost'):
#             tests.fill_in_exchange_ber_cost(driver)
#
#     def test_fill_exchange_lead_time(self, driver):
#         with pytest.allure.step('Fill exchange lead time'):
#             tests.fill_in_exchange_lead_time(driver)
#
#     def test_fill_exchange_cost_total(self, driver):
#         with pytest.allure.step('Fill exchange cost total'):
#             tests.fill_in_exchange_cost_total(driver)
#
#     def test_fill_exchange_qty(self, driver):
#         with pytest.allure.step('Fill exchange qty'):
#             tests.fill_in_exchange_qty(driver)
#
#     def test_fill_ex_fee_price(self, driver):
#         with pytest.allure.step('Fill exchange fee price'):
#             tests.fill_in_exchange_fee_price(driver)
#
#     def test_fill_exchange_cust_rtrn_days(self, driver):
#         with pytest.allure.step('Fill exchange cust rtrn days'):
#             tests.fill_in_exchange_cust_rtrn_days(driver)
#
#     def test_fill_exchange_service_prive(self, driver):
#         with pytest.allure.step('Fill exchange service price'):
#             tests.fill_in_exchange_service_price(driver)
#
#     def test_fill_exchange_ber_price(self, driver):
#         with pytest.allure.step('Fill exhange ber price'):
#             tests.fill_in_exchange_ber_price(driver)
#
#     def test_fill_exchange_delivery_time(self, driver):
#         with pytest.allure.step('Fill exchange delivery time'):
#             tests.fill_in_exchange_delivery_time(driver)
#
#     def test_fill_exchange_plli_aval_qty(self, driver):
#         with pytest.allure.step('Fill Exchange Aval.Qty'):
#             tests.fill_in_plli_aval_qty(driver)
#
#     def test_fill_exchange_notes(self, driver):
#         with pytest.allure.step('Fill stock outright notes'):
#             tests.fill_note(driver)
#
#     def test_fill_exchange_non_print_notes(self, driver):
#         with pytest.allure.step('Fill non printed notes'):
#             tests.fill_non_printed_note(driver)
#
#     def test_fill_exchange_v_quote_notes(self, driver):
#         with pytest.allure.step('Fill Exchange V.Quote'):
#             tests.fill_v_quote(driver)
#
# # Repair
#     def test_click_alt_offer_repair(self, driver):
#         with pytest.allure.step('Click alt offer'):
#             tests.click_alt_offer(driver)
#
#     def test_select_repair(self, driver):
#         with pytest.allure.step('Select repair type'):
#             tests.select_repair_type(driver)
#
#     def test_fill_bcheck_price(self, driver):
#         with pytest.allure.step('Fill repair bcheck cost'):
#             tests.fill_in_repair_bcheck_cost(driver)
#
#     def test_fill_lead_bcheck(self, driver):
#         with pytest.allure.step('Fill repair lead b check'):
#             tests.fill_in_repair_lead_b_check(driver)
#
#     def test_fill_avg_repair_cost(self, driver):
#         with pytest.allure.step('Fill avg repair price'):
#             tests.fill_in_avg_repair_price(driver)
#
#     def test_fill_max_repair_cost(self, driver):
#         with pytest.allure.step('Fill max repair cost'):
#             tests.fill_in_max_repair_cost(driver)
#
#     def test_fill_repair_lead_time(self, driver):
#         with pytest.allure.step('Fill repair lead time'):
#             tests.fill_in_repair_lead_time(driver)
#
#     def test_fill_repair_qty(self, driver):
#         with pytest.allure.step('Fill repair qty'):
#             tests.fill_in_repair_qty(driver)
#
#     def test_repair_bcheck_price(self, driver):
#         with pytest.allure.step('Fill repair bcheck price'):
#             tests.fill_in_repair_bcheck_price(driver)
#
#     def test_fill_delivery_bcheck(self, driver):
#         with pytest.allure.step('Fill repair delivery b check'):
#             tests.fill_in_repair_delivery_b_check(driver)
#
#     def test_fill_avg_repair_price(self, driver):
#         with pytest.allure.step('Fill avg repair price'):
#             tests.fill_in_avg_repair_price(driver)
#
#     def test_fill_max_repair_price(self, driver):
#         with pytest.allure.step('Fill max repair price'):
#             tests.fill_in_max_repair_price(driver)
#
#     def test_fill_repair_delivery_time(self, driver):
#         with pytest.allure.step('Fill repair delivery time'):
#             tests.fill_in_repair_delivery_time(driver)
#
#     def test_fill_repair_plli_aval_qty(self, driver):
#         with pytest.allure.step('Fill Repair Aval.Qtyu'):
#             tests.fill_in_plli_aval_qty(driver)
#
#     def test_fill_repair_notes(self, driver):
#         with pytest.allure.step('Fill repair notes'):
#             tests.fill_note(driver)
#
#     def test_fill_repair_non_print_notes(self, driver):
#         with pytest.allure.step('Fill repair notes'):
#             tests.fill_non_printed_note(driver)
#
#     def test_fill_repair_v_quote_notes(self, driver):
#         with pytest.allure.step('Fill Repair V.Quote'):
#             tests.fill_v_quote(driver)
#
#     def test_click_save_rfq(self, driver):
#         with pytest.allure.step('Click save rfq'):
#             tests.click_save_rfq(driver)

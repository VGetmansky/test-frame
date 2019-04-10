import pytest
from crm.tests import invoice_tests as tests
from crm.scenarios.login_scenario import TestLogInApp
from crm.scenarios.work_with_so import TestWorkWithSOList

TestLogInApp()
# TestWorkWithSOList()


@pytest.mark.test
class TestOpenSODetails:
    def test_open_so_tab(self, driver):
        with pytest.allure.step('Open URL'):
            tests.select_so(driver)

    def test_open_so_details(self, driver, url):
        with pytest.allure.step('Open SO details'):
            tests.open_so_details(driver, url)


@pytest.allure.testcase('Work With Quotes')
@pytest.mark.test
class TestCreateInvoice:

    def test_click_add_invoice(self, driver):
        with pytest.allure.step('Click add invoice'):
            tests.click_add_invoice(driver)

    def test_fill_invoice_no(self, driver):
        with pytest.allure.step('Fill invoice no'):
            tests.fill_in_invoice_no(driver)

    def test_fill_customer_po(self, driver):
        with pytest.allure.step('Fill customer PO'):
            tests.fill_in_customer_po(driver)

    def test_fill_customer_no(self, driver):
        with pytest.allure.step('Fill customer no'):
            tests.fill_in_customer_no(driver)

    def test_select_terms_of_sale(self, driver, url):
        with pytest.allure.step('Select terms of sale'):
            tests.select_terms_of_sale(driver, url)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            tests.select_priority(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select terms of delivery'):
            tests.select_terms_of_delivery(driver)

    def test_fill_sales_commission(self, driver):
        with pytest.allure.step('Fill sales commission'):
            tests.fill_in_sales_commision(driver)

    def test_fill_account(self, driver):
        with pytest.allure.step('Fill account'):
            tests.fill_in_account(driver)

    def test_fill_boxes(self, driver):
        with pytest.allure.step('Fill boxes'):
            tests.fill_in_boxes(driver)

    def test_fill_dimensions(self, driver):
        with pytest.allure.step('Fill dimensions'):
            tests.fill_in_dimensions(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select territory'):
            tests.select_territory(driver)

    def test_select_due_date(self, driver):
        with pytest.allure.step('Select due date'):
            tests.select_due_date(driver)

    def test_select_status(self, driver, url):
        with pytest.allure.step('Select status'):
            tests.select_status(driver, url)

    def test_fill_place_of_delivery(self, driver):
        with pytest.allure.step('Fill place of delivery'):
            tests.fill_in_place_of_delivery(driver)

    def test_select_ship_via(self, driver):
        with pytest.allure.step('Select ship via'):
            tests.select_ship_via(driver)

    def test_fill_awb(self, driver):
        with pytest.allure.step('Fill awb'):
            tests.fill_in_awb(driver)

    def test_fill_weight(self, driver):
        with pytest.allure.step('Fill weight'):
            tests.fill_in_weight(driver)

    def test_fill_invoice_date(self, driver):
        with pytest.allure.step('Select invoice date'):
            tests.select_invoice_date(driver)

    def test_fill_order_date(self, driver):
        with pytest.allure.step('Select order date'):
            tests.select_order_date(driver)

    def test_fill_total_payments(self, driver):
        with pytest.allure.step('Fill total payments'):
            tests.fill_in_total_payments(driver)

    def test_fill_percent_paid(self, driver):
        with pytest.allure.step('Fill percent paid'):
            tests.fill_in_percent_paid(driver)

    def test_fill_in_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            tests.fill_in_billing_address(driver)

    def test_fill_in_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            tests.fill_in_shipping_address(driver)

    def test_fill_in_billing_po_box(self, driver):
        with pytest.allure.step('Fill billing po box'):
            tests.fill_in_billing_po_box(driver)

    def test_fill_in_billing_city(self, driver):
        with pytest.allure.step('Fill billing city'):
            tests.fill_in_billing_city(driver)

    def test_fill_in_billing_state(self, driver):
        with pytest.allure.step('Fill billing state'):
            tests.fill_in_billing_state(driver)

    def test_fill_in_billing_post_code(self, driver):
        with pytest.allure.step('Fill billing post code'):
            tests.fill_in_billing_post_code(driver)

    def test_fill_in_billing_post_country(self, driver):
        with pytest.allure.step('Fill billing country'):
            tests.fill_in_billing_country(driver)

    def test_fill_in_shipping_po_box(self, driver):
        with pytest.allure.step('Fill shipping po box'):
            tests.fill_in_shipping_po_box(driver)

    def test_fill_in_shipping_city(self, driver):
        with pytest.allure.step('Fill shipping city'):
            tests.fill_in_shipping_city(driver)

    def test_fill_in_shipping_state(self, driver):
        with pytest.allure.step('Fill shipping state'):
            tests.fill_in_shipping_state(driver)

    def test_fill_in_shipping_post_code(self, driver):
        with pytest.allure.step('Fill shipping post code'):
            tests.fill_in_shipping_post_code(driver)

    def test_fill_in_shipping_post_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            tests.fill_in_shipping_country(driver)

    def test_fill_special_notes(self, driver):
        with pytest.allure.step('Fill special note'):
            tests.fill_in_special_note(driver)

    def test_click_save_button(self, driver):
        with pytest.allure.step('Click save invoice button'):
            tests.click_save_button(driver)

    def test_check_values(self, driver):
        with pytest.allure.step('check values'):
            tests.check_values(driver)

    def test_open_invoice_details(self, driver):
        with pytest.allure.step('Open Invoice Details'):
            tests.open_invoice_list(driver)
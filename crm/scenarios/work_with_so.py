import pytest
from crm.tests import so_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With SO')
@pytest.mark.test
class TestWorkWithSOList:
    def test_open_so_tab(self, driver):
        with pytest.allure.step('Select SO'):
            tests.select_sales_orders(driver)


@pytest.mark.test
class TestClickAddButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add SO'):
            tests.click_add_so(driver, url)


@pytest.mark.test
class TestCreateSO:

    def test_select_account(self, driver):
        with pytest.allure.step('Fill account field'):
            tests.fill_in_account_field(driver)

    def test_select_contact_name(self, driver):
        with pytest.allure.step('Select Contact Name'):
            tests.select_contact_name(driver)

    def test_select_customer_quote(self, driver):
        with pytest.allure.step('Select Customer Quote'):
            tests.select_customer_quote(driver)

    def test_select_location(self, driver):
        with pytest.allure.step('Select Location'):
            tests.select_location(driver)

    def test_select_aircraft(self, driver):
        with pytest.allure.step('Select Aircraft'):
            tests.select_aircraft(driver)

    def test_select_assets(self, driver):
        with pytest.allure.step('Select Assets'):
            tests.select_assets(driver)

    def test_select_sold_by(self, driver):
        with pytest.allure.step('Select Sold By'):
            tests.select_sold_by(driver)

    def test_select_status(self, driver):
        with pytest.allure.step('Select Status'):
            tests.select_status(driver)

    def test_select_terms_of_payment(self, driver):
        with pytest.allure.step('Select Terms Of Payment'):
            tests.select_terms_of_payment(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            tests.select_priority(driver)

    def test_select_ship_via(self, driver):
        with pytest.allure.step('Select Ship Via'):
            tests.select_ship_via(driver)

    def test_select_assigned_to(self, driver):
        with pytest.allure.step('Select Assigned To'):
            tests.select_assigned_to(driver)

    def test_fill_place_of_delivery(self, driver):
        with pytest.allure.step('FIll Place of Delivery'):
            tests.fill_in_place_of_delivery(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select Terms Of Delivery'):
            tests.select_terms_of_delivery(driver)

    def test_fill_sales_commission(self, driver):
        with pytest.allure.step('FIll Sales Commission'):
            tests.fill_in_sales_commission(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select Territory'):
            tests.select_territory(driver)

    def test_fill_account_number(self, driver):
        with pytest.allure.step('FIll Account Number'):
            tests.fill_in_account_number(driver)

    def test_fill_in_client_po(self, driver):
        with pytest.allure.step('Fill client PO'):
            tests.fill_in_client_po(driver)

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

    def test_fill_in_so_notice(self, driver):
        with pytest.allure.step('Fill SO Notice'):
            tests.fill_in_so_notes(driver)

    def test_add_product(self, driver):
        with pytest.allure.step('Add product'):
            tests.add_product(driver)

    def test_save_so(self, driver):
        with pytest.allure.step('Save SO'):
            tests.save_so(driver)

# go to home page

    # def test_close_alert(self, driver):
    #     tests.close_alert(driver)

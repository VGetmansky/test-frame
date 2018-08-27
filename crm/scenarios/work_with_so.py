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

    def test_fill_in_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            tests.fill_in_billing_address(driver)

    def test_fill_in_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            tests.fill_in_shipping_address(driver)

    def test_select_account(self, driver):
        with pytest.allure.step('Fill account field'):
            tests.fill_in_account_field(driver)

    def test_select_contact_name(self, driver):
        with pytest.allure.step('Select Contact Name'):
            tests.select_contact_name(driver)

    def test_add_product(self, driver):
        with pytest.allure.step('Add product'):
            tests.add_product(driver)

    def test_fill_in_client_po(self, driver):
        with pytest.allure.step('Fill client PO'):
            tests.fill_in_client_po(driver)

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

    def test_save_so(self, driver):
        with pytest.allure.step('Save SO'):
            tests.save_so(driver)

# go to home page

    # def test_close_alert(self, driver):
    #     tests.close_alert(driver)

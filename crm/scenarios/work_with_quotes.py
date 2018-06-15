import pytest
from crm.tests import quotest_tests as tests
from crm.scenarios.login_scenario import TestLogInApp

TestLogInApp()


@pytest.allure.testcase('Work With Quotes')
@pytest.mark.test
class TestWorkWithQuotesList:
    def test_open_quotes_tab(self, driver):
        with pytest.allure.step('Select quote'):
            tests.select_quote(driver)


@pytest.mark.test
class TestClickAddButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add quote'):
            tests.click_add_quote(driver, url)


@pytest.mark.test
class TestCreateQuote:

    def test_select_account(self, driver):
        with pytest.allure.step('Fill Account'):
            tests.fill_in_account_field(driver)

    def test_fill_in_cust_ref(self, driver):
        with pytest.allure.step('Fill cust ref'):
            tests.fill_in_cust_ref(driver)

    def test_fill_in_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            tests.fill_in_billing_address(driver)

    def test_fill_in_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            tests.fill_in_shipping_address(driver)

    def test_fill_in_place_of_delivery(self, driver):
        with pytest.allure.step('Fill place of delivery'):
            tests.fill_in_place_of_delivery(driver)

    def test_select_quote_status(self,driver):
        with pytest.allure.step('Select quote status'):
            tests.select_quote_status(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            tests.select_proirity(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select terms of delivery'):
            tests.select_terms_of_delivery(driver)

    def test_select_terms_of_sale(self, driver):
        with pytest.allure.step('Select terms sale'):
            tests.select_terms_sale(driver)

    def test_add_product(self, driver):
        with pytest.allure.step('Add product'):
            tests.add_product(driver)

    # def test_close_alert(self, driver):
    #     tests.close_alert(driver)

    def test_fill_in_billing_po_box(self, driver):
        with pytest.allure.step('Fill billing box'):
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
        with pytest.allure.step('Fill shipping box'):
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

    def test_fill_in_description_details(self, driver):
        with pytest.allure.step('Fill description details'):
            tests.fill_in_description_details(driver)

    def test_save_so(self, driver):
        with pytest.allure.step('Save SO'):
            tests.save_so(driver)


@pytest.mark.test
class TestClickCreateQuoteButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add quote'):
            tests.click_add_quote(driver, url)

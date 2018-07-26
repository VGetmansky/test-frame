import pytest
from crm.tests import accounts_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With Accounts')
@pytest.mark.test
class TestWorkWithAccountList:
    def test_open_accounts_tab(self, driver):
        with pytest.allure.step('Select Accounts'):
            tests.select_accounts(driver)


@pytest.allure.testcase('Add Account')
@pytest.mark.test
class TestAddNewAccount:
    def test_click_add_new_account_tab(self, driver, url):
        with pytest.allure.step('Click Add New Account'):
            tests.click_add_account(driver, url)

    def test_fill_account_name(self, driver, url):
        with pytest.allure.step('Fill Account Name'):
            tests.fill_account_name(driver, url)

    # def test_website(self, driver, url):
    #     with pytest.allure.step('Fill Website'):
    #         tests.fill_website(driver, url)

    def test_fill_ticker_symbol(self, driver):
        with pytest.allure.step('Fill Ticker Symbol'):
            tests.fill_ticker_symbol(driver)

    def test_select_member_of(self, driver):
        with pytest.allure.step('Select Member Of'):
            tests.fill_in_member_of(driver)

    def test_fill_fleet_size(self, driver):
        with pytest.allure.step('Select Fleet size'):
            tests.fill_fleet_size(driver)

    def test_fill_secondary_email(self, driver):
        with pytest.allure.step('Fill secondary email'):
            tests.fill_secondary_email(driver)

    def test_select_industry(self, driver):
        with pytest.allure.step('Select indutry'):
            tests.select_industry(driver)

    def test_select_type(self, driver):
        with pytest.allure.step('Select type'):
            tests.select_type(driver)

    def test_check_email_opt_out(self, driver):
        with pytest.allure.step('Check Email Opt Out'):
            tests.check_email_opt_out(driver)

    def test_select_assigned_to(self, driver):
        with pytest.allure.step('Select Assigned To'):
            tests.select_assigned_to(driver)

    def test_fill_account_number(self, driver):
        with pytest.allure.step('Fill Account_number'):
            tests.fill_account_number(driver)

    def test_fill_primary_phone(self, driver):
        with pytest.allure.step('Fill Primary Phone'):
            tests.fill_primary_phone(driver)

    def test_fill_fax(self, driver):
        with pytest.allure.step('Fill Fax'):
            tests.fill_fax(driver)

    def test_fill_secondary_phone(self, driver):
        with pytest.allure.step('Fill secondary phone'):
            tests.fill_secondary_phone(driver)

    def test_fill_primary_email(self, driver):
        with pytest.allure.step('Fill Primary Email'):
            tests.fill_primary_email(driver)

    def test_fill_ownership(self, driver):
        with pytest.allure.step('Fill Ownership'):
            tests.fill_ownership(driver)

    def test_select_rating(self, driver):
        with pytest.allure.step('Select Rating'):
            tests.select_rating(driver)

    def test_fill_sic_code(self, driver):
        with pytest.allure.step('Fill SIC Code'):
            tests.fill_sic_code(driver)

    def test_fill_annual_revenue(self, driver):
        with pytest.allure.step('Fill Annual_Revenue'):
            tests.fill_annual_revenue(driver)

    def test_check_notify_owner(self, driver):
        with pytest.allure.step('Check Notify Owner'):
            tests.check_notify_owner(driver)


# ------------------ Account Details ------------------

    def test_check_sync_to_qb(self, driver):
        with pytest.allure.step('Check sync to QB'):
            tests.check_sync_to_qb(driver)

    def test_select_qb_customer_type(self, driver):
        with pytest.allure.step('Select QB Customer Type'):
            tests.select_qb_customer_type(driver)

    def test_check_sent_to_qb(self, driver):
        with pytest.allure.step('Check Sent To QB'):
            tests.check_sent_to_qb(driver)

    def test_check_taxable(self, driver):
        with pytest.allure.step('Check Taxable'):
            tests.check_taxable(driver)


# ------------------ Pricing Information ------------------

    def test_fill_tear_1_max(self, driver):
        with pytest.allure.step('Fill Tear 1 Max'):
            tests.fill_tear_1_max(driver)

    def test_fill_tear_2_max(self, driver):
        with pytest.allure.step('Fill Tear 2 Max'):
            tests.fill_tear_2_max(driver)

    def test_fill_tear_3_max(self, driver):
        with pytest.allure.step('Fill Tear 3 Max'):
            tests.fill_tear_3_max(driver)

    def test_fill_tear_4_max(self, driver):
        with pytest.allure.step('Fill Tear 4 Max'):
            tests.fill_tear_4_max(driver)

    def test_fill_tear_1_ratio(self, driver):
        with pytest.allure.step('Fill Tear 1 ratio'):
            tests.fill_tear_1_ratio(driver)

    def test_fill_tear_2_ratio(self, driver):
        with pytest.allure.step('Fill Tear 2 ratio'):
            tests.fill_tear_2_ratio(driver)

    def test_fill_tear_3_ratio(self, driver):
        with pytest.allure.step('Fill Tear 3 ratio'):
            tests.fill_tear_3_ratio(driver)

    def test_fill_tear_4_ratio(self, driver):
        with pytest.allure.step('Fill Tear 4 ratio'):
            tests.fill_tear_4_ratio(driver)


# ------------------ Custom Information ------------------

    def test_select_qb_company(self, driver):
        with pytest.allure.step('Select QB Company'):
            tests.select_qb_company(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select Terms Of Delivery'):
            tests.select_terms_of_delivery(driver)

    def test_fill_recieved_via(self, driver):
        with pytest.allure.step('Fill Recieved VIA'):
            tests.fill_recieved_via(driver)

    def test_select_terms_of_sale(self, driver):
        with pytest.allure.step('Select Terms Of Sale'):
            tests.select_terms_of_sale(driver)

    def test_fill_place_of_delivery(self, driver):
        with pytest.allure.step('Fill Place of Delivery'):
            tests.fill_place_of_delivery(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('Select Territory'):
            tests.select_territory(driver)


# ------------------ Address Details ------------------

    def test_fill_billing_address(self, driver):
        with pytest.allure.step('Fill billing address'):
            tests.fill_billing_address(driver)

    def test_fill_billing_po_box(self, driver):
        with pytest.allure.step('Fill billing po_box'):
            tests.fill_billing_po_box(driver)

    def test_fill_billing_city(self, driver):
        with pytest.allure.step('Fill billing city'):
            tests.fill_billing_city(driver)

    def test_fill_billing_state(self, driver):
        with pytest.allure.step('Fill billing state'):
            tests.fill_billing_state(driver)

    def test_fill_billing_postal_code(self, driver):
        with pytest.allure.step('Fill billing code'):
            tests.fill_billing_postal_code(driver)

    def test_fill_billing_country(self, driver):
        with pytest.allure.step('Fill billing country'):
            tests.fill_billing_country(driver)

    def test_fill_shipping_address(self, driver):
        with pytest.allure.step('Fill shipping address'):
            tests.fill_shipping_address(driver)

    def test_fill_shipping_po_box(self, driver):
        with pytest.allure.step('Fill shipping po_box'):
            tests.fill_shipping_po_box(driver)

    def test_fill_shipping_city(self, driver):
        with pytest.allure.step('Fill shipping city'):
            tests.fill_shipping_city(driver)

    def test_fill_shipping_state(self, driver):
        with pytest.allure.step('Fill shipping state'):
            tests.fill_shipping_state(driver)

    def test_fill_shipping_postal_code(self, driver):
        with pytest.allure.step('Fill shipping code'):
            tests.fill_shipping_postal_code(driver)

    def test_fill_shipping_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            tests.fill_shipping_country(driver)

# ------------------ Description Details ------------------

    def test_fill_description(self, driver):
        with pytest.allure.step('Fill Description'):
            tests.fill_description(driver)

    def test_save_account(self, driver):
        with pytest.allure.step('Click Save Account'):
            tests.click_save_account(driver)

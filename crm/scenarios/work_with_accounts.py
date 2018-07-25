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
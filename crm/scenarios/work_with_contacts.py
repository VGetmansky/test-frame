import pytest
from crm.tests import contacts_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With Contacts')
@pytest.mark.test
class TestWorkWithContactsList:
    def test_open_contacts_tab(self, driver):
        with pytest.allure.step('Select Contacts'):
            tests.select_contacts(driver)

@pytest.mark.test
class TestClickAddContactsButton:
    def test_click_add_contact_button(self, driver, url):
        with pytest.allure.step('Click add Contact'):
            tests.click_add_contact(driver, url)
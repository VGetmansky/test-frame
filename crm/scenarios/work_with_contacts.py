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

    def test_click_fill_contact_first_name(self, driver):
        with pytest.allure.step('Fill First Name'):
            tests.fill_contact_first_name(driver)

    def test_click_fill_contact_last_name(self, driver):
        with pytest.allure.step('Fill Last Name'):
            tests.fill_contact_last_name(driver)

    def test_click_fill_contact_title(self, driver):
        with pytest.allure.step('Fill Contact Title'):
            tests.fill_contact_title(driver)

    def test_click_fill_contact_department(self, driver):
        with pytest.allure.step('Fill Contact Department'):
            tests.fill_contact_department(driver)

    def test_click_fill_primary_email(self, driver):
        with pytest.allure.step('Fill Primary Email'):
            tests.fill_contact_primary_email(driver)

    def test_click_fill_contact_assistant(self, driver):
        with pytest.allure.step('Fill Contact Assistant'):
            tests.fill_contact_assistant(driver)

    def test_click_fill_contact_assistant_phone(self, driver):
        with pytest.allure.step('Fill Contact Assistant Phone'):
            tests.fill_contact_assistant_phone(driver)

    def test_click_fill_role(self, driver):
        with pytest.allure.step('Fill Role'):
            tests.fill_contact_role(driver)

    def test_click_fill_contact_id(self, driver):
        with pytest.allure.step('Fill Role'):
            tests.fill_contact_id(driver)

    def test_click_office_phone(self, driver):
        with pytest.allure.step('Fill office phone'):
            tests.fill_office_phone(driver)

    def test_click_fill_mobile_phone(self, driver):
        with pytest.allure.step('Fill Mobile Phone'):
            tests.fill_contact_mobile_phone(driver)

    def test_click_fill_home_phone(self, driver):
        with pytest.allure.step('Fill Home Phone'):
            tests.fill_contact_home_phone(driver)

    def test_click_fill_secondary_phone(self, driver):
        with pytest.allure.step('Fill Secondary Phone'):
            tests.fill_contact_secondary_phone(driver)

    def test_click_fill_contact_fax(self, driver):
        with pytest.allure.step('Fill Fax'):
            tests.fill_contact_fax(driver)

    def test_click_fill_secondary_email(self, driver):
        with pytest.allure.step('Fill Secondary Email'):
            tests.fill_contact_secondary_email(driver)

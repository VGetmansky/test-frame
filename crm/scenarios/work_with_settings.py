import pytest
from crm.tests import adm_settings_test as tests
from crm.scenarios.login_scenario import TestLogInApp


@pytest.allure.testcase('Work With Settings')
@pytest.mark.test
class TestWorkWithSettingsMenu:
    def test_click_settings_tab(self, driver):
        with pytest.allure.step('Click Settings '):
            tests.click_settings(driver)

    def test_select_crm_settings(self, driver):
        with pytest.allure.step('Click CRM Settings'):
            tests.select_crm_settings(driver)


@pytest.allure.testcase('Work With Studio')
@pytest.mark.test
class TestWorkWithStudio:
    def test_select_studio_category(self, driver):
        with pytest.allure.step('Click studio category'):
            tests.select_studio_category(driver)

    def test_select_edit_fields(self, driver):
        with pytest.allure.step('Click Edit Fields'):
            tests.select_edit_fields(driver)

    def test_click_opportunities(self, driver):
        with pytest.allure.step('Click Edit Fields'):
            tests.click_opportunities(driver)

    def test_click_contacts(self, driver):
        with pytest.allure.step('Click Edit Fields'):
            tests.click_contacts(driver)

import pytest
from crm.tests import material_arrival_tests as tests
from crm.scenarios.login_scenario import TestLogInApp

TestLogInApp()


@pytest.allure.testcase('Work With Material Arrival')
@pytest.mark.test
class TestWorkWithMaterialArrival:
    def test_click_category_all_material_arrival(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_material_arrival(self, driver, url):
        with pytest.allure.step('Select Material Arrival'):
            tests.select_material_arrival_category(driver, url)

    def test_fill_vendor(self, driver):
        with pytest.allure.step('Select Vendor'):
            tests.select_vendor(driver)

    def test_filter_by_last_po(self, driver):
        with pytest.allure.step('Filter List by Last PO'):
            tests.filter_by_last_po(driver)

    def test_check_po_checkboxes(self, driver):
        with pytest.allure.step('Check PO Checkboxes'):
            tests.check_po_checkboxes(driver)

    def test_click_category_all_shipping_notice(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_shipping_notice(self, driver, url):
        with pytest.allure.step('Select Shipping Notice'):
            tests.select_shipping_notice_category(driver, url)

    def test_select_accoount(self, driver, url):
        with pytest.allure.step('Select Account'):
            tests.select_account(driver)

    def test_filter_by_last_so(self, driver):
        with pytest.allure.step('Filter List by Last SO'):
            tests.filter_by_last_so(driver)
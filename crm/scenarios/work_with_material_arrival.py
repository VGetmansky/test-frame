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

    def test_shipping_notice_add_note(self, driver):
        with pytest.allure.step('Add note'):
            tests.filter_add_note(driver)

    def test_check_po_checkboxes(self, driver):
        with pytest.allure.step('Check SO Checkboxes'):
            tests.check_shipping_notice_so_checkboxes(driver)

    def test_click_category_all_inspection(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_inspection(self, driver, url):
        with pytest.allure.step('Select Inspection'):
            tests.select_inspection_category(driver, url)

    # def test_inspection_add_note(self, driver):
    #     with pytest.allure.step('Add Inspection note'):
    #         tests.filter_add_note(driver)

    def test_select_last_inspection(self, driver, url):
        with pytest.allure.step('Select Last Inspection'):
            tests.filter_by_last_inspection(driver, "inspection")

    def test_filter_inspection_by_last_so(self, driver):
        with pytest.allure.step('Filter Inspection List by newest SO'):
            tests.filter_by_last_so(driver)

    def test_check_inspection_checkboxes(self, driver):
        with pytest.allure.step('Check inspection SO Checkboxes'):
            tests.select_all_material_arrival_inspection(driver)

    def test_click_category_all_receiving(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_receiving(self, driver, url):
        with pytest.allure.step('Select Receiving'):
            tests.select_receiving(driver, url)

    def test_select_last_receiving(self, driver, url):
        with pytest.allure.step('Select Last Receiving'):
            tests.filter_by_last_inspection(driver, "receiving")

    def test_filter_receiving_by_last_so(self, driver):
        with pytest.allure.step('Filter Receiving List by newest SO'):
            tests.filter_by_last_so(driver)

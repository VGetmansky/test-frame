import pytest
from crm.tests import material_arrival_tests as tests
from crm.scenarios.login_scenario import TestLogInApp

TestLogInApp()


@pytest.allure.testcase('Work With Material Arrival')
@pytest.mark.test
class TestWorkWithMaterialArrival:

    #  ----------   Material Arrival     ----------

    def test_click_category_all_material_arrival(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_material_arrival(self, driver, url):
        with pytest.allure.step('Select Material Arrival'):
            tests.select_material_arrival_category(driver, url)

    def test_open_test_url(self, driver, url):
        with pytest.allure.step('Open test MA '):
            tests.open_qatest_url(driver)

    def test_fill_material_arrival_vendor(self, driver):
        with pytest.allure.step('Select Vendor'):
            tests.select_vendor(driver)

    def test_expand_last_vendor_material_arrival_po(self, driver):
        with pytest.allure.step('Expand PO'):
            tests.expand_po_list(driver)

    # def test_material_arrival_get_last_po(self, driver):
    #     with pytest.allure.step('Get newesst PO number'):
    #         tests.get_newest_po_number(driver)

    def test_fill_material_arrival_po(self, driver):
        with pytest.allure.step('Select PO'):
            tests.select_po(driver, "P53323  ")

    def test_expand_po_details(self, driver):
        with pytest.allure.step('Expand PO'):
            tests.expand_po_list(driver)

    def test_check_all_ma_partnumbers(self, driver):
        with pytest.allure.step('Check all PN'):
            tests.check_all_ma_partnumbers(driver, "PO")

    def test_set_arrived_qty(self, driver):
        with pytest.allure.step('Set arrived qty'):
            tests.fill_arrived_qty(driver)

    def test_click_material_arrival_deliver(self, driver):
        with pytest.allure.step('Click Deliver MA'):
            tests.click_material_arrival_deliver(driver)

    #  ----------   Material Arrival History     ----------

    def test_check_delivered_material_arrival(self, driver):
        with pytest.allure.step('Check Delivered MA Values'):
            tests.check_delivered_material_arrival(driver)

    def test_click_material_arrival_notice(self, driver):
        with pytest.allure.step('Click Go to notice button'):
            tests.click_material_arrival_notice(driver)
    #
    # def test_click_material_arrival_inspection(self, driver):
    #     with pytest.allure.step('Click Notice Go to Inspection'):
    #         tests.click_material_arrival_inspection(driver)
    #

    # #  ----------   Shipping Notice     ----------

    #
    # def test_click_category_all_shipping_notice(self, driver):
    #     with pytest.allure.step('Select all'):
    #         tests.click_all_category(driver)
    #
    # def test_click_shipping_notice(self, driver, url):
    #     with pytest.allure.step('Select Shipping Notice'):
    #         tests.select_shipping_notice_category(driver, url)
    #
    # def test_select_accoount(self, driver):
    #     with pytest.allure.step('Select Account'):
    #         tests.select_account(driver)
    #
    # def test_filter_by_last_so(self, driver):
    #     with pytest.allure.step('Filter List by Last SO'):
    #         tests.filter_by_last_so(driver)
    #
    # def test_shipping_notice_add_note(self, driver):
    #     with pytest.allure.step('Add note'):
    #         tests.filter_add_note(driver)
    #
    # def test_check_shipping_notice_po_checkboxes(self, driver):
    #     with pytest.allure.step('Check SO Checkboxes'):
    #         tests.check_shipping_notice_so_checkboxes(driver)
    #
    # def test_click_send_notice(self, driver):
    #     with pytest.allure.step('Click Material Arrival Send Notice'):
    #         tests.click_material_arrival_send_notice(driver)
    #
    #  ----------   Inspection     ----------

    def test_click_category_all_inspection(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_inspection(self, driver, url):
        with pytest.allure.step('Select Inspection'):
            tests.select_inspection_category(driver, url)

    def test_select_last_inspection(self, driver):
        with pytest.allure.step('Select Last Inspection'):
            tests.filter_by_last_inspection(driver, "inspection")

    def test_filter_inspection_by_last_so(self, driver):
        with pytest.allure.step('Filter Inspection List by newest SO'):
            tests.filter_by_last_so(driver)

    def test_check_inspection_checkboxes(self, driver):
        with pytest.allure.step('Check inspection SO Checkboxes'):
            tests.select_all_material_arrival_inspection(driver)

    def test_click_approve(self, driver):
        with pytest.allure.step('Click Material Arrival Approve'):
            tests.click_material_arrival_approve(driver)

    #  ----------   Receiving     ----------

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

    def test_select_all_material_arrival_receiving(self, driver):
        with pytest.allure.step('Select All MA Receiving'):
            tests.select_all_material_arrival_chkboxes(driver)

    def test_click_receive(self, driver):
        with pytest.allure.step('Click Material Arrival Receive'):
            tests.click_material_arrival_receive(driver)

    #  ----------   Packing     ----------

    def test_click_category_all_packing(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_packing(self, driver, url):
        with pytest.allure.step('Select Packing'):
            tests.select_receiving(driver, url)

    def test_select_last_packing(self, driver, url):
        with pytest.allure.step('Select Last Packing'):
            tests.filter_by_last_inspection(driver, "packing")

    def test_filter_packing_by_last_so(self, driver):
        with pytest.allure.step('Filter Packing List by newest SO'):
            tests.filter_by_last_so(driver)

    def test_select_all_material_arrival_packing(self, driver):
        with pytest.allure.step('Select All MA Packing'):
            tests.select_all_material_arrival_chkboxes(driver)

    def test_fill_material_arrival_warehouse_index(self, driver):
        with pytest.allure.step('Fill Warehouse Index'):
            tests.fill_material_arrival_warehouse_index(driver)

    def test_click_packing_receive(self, driver):
        with pytest.allure.step('Click Material Arrival Receive'):
            tests.click_material_arrival_receive(driver)
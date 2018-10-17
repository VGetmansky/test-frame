import pytest
from crm.tests import po_tests as tests
from crm.scenarios.login_scenario import TestLogInApp
import allure


@pytest.allure.testcase('Work With SO')
@pytest.mark.test
class TestWorkWithPOList:
    def test_open_po_tab(self, driver):
        with pytest.allure.step('Open URL'):
            tests.select_po(driver)


@pytest.mark.test
class TestClickAddPO:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Open URL'):
            tests.click_add_po(driver, url)


@pytest.mark.test
class TestCreatePO:

    def test_select_vendor(self, driver):
        with pytest.allure.step('Select Vendor'):
            tests.select_vendor(driver)

    def test_copy_vendor_address(self, driver):
        with pytest.allure.step('Copy Vendor Address'):
            tests.copy_vendor_address(driver)

    def test_copy_company_address(self, driver):
        with pytest.allure.step('Copy Company Address'):
            tests.copy_company_address(driver)

    def test_fill_vendor_po(self, driver):
        with pytest.allure.step('Fill Vendor PO'):
            tests.fill_in_vendor_po(driver)

    def test_fill_tracking_number(self, driver):
        with pytest.allure.step('Fill tracking number'):
            tests.fill_in_tracking_number(driver)

    def test_select_priority(self, driver):
        with pytest.allure.step('Select priority'):
            tests.select_priority(driver)

    def test_fill_account(self, driver):
        with pytest.allure.step('Fill account'):
            tests.fill_in_account(driver)

    def test_select_status(self, driver):
        with pytest.allure.step('Select Status'):
            tests.select_status(driver)

    def test_select_terms_of_payment(self, driver, url):
        with pytest.allure.step('select terms of payment'):
            tests.select_terms_of_payment(driver, url)

    def test_select_due_date(self, driver):
        with pytest.allure.step('Due date'):
            tests.select_due_date(driver)

    def test_select_aircraft(self, driver):
        with pytest.allure.step('Aircraft'):
            tests.select_aircraft(driver)

    def test_fill_po_number(self, driver):
        with pytest.allure.step('fill po number'):
            tests.fill_in_po_number(driver)

    def test_fill_requisition_number(self, driver):
        with pytest.allure.step('Fill requisition number'):
            tests.fill_in_requisition_number(driver)

    def test_select_contact_name(self, driver):
        with pytest.allure.step('Select contact name'):
            tests.select_contact_name(driver)

    def test_select_ship_via(self, driver):
        with pytest.allure.step('Select ship via'):
            tests.select_ship_via(driver)

    def test_fill_sales_commission(self, driver):
        with pytest.allure.step('Fill sales commission'):
            tests.fill_in_sales_commission(driver)

    def test_excise_duty(self, driver):
        with pytest.allure.step('Fill excise duty'):
            tests.fill_in_excise_duty(driver)

    # def test_select_assigned_to(self, driver):
    #     tests.select_assigned_to(driver)

    def test_select_terms_of_delivery(self, driver):
        with pytest.allure.step('Select terms of delivery'):
            tests.select_terms_of_delivery(driver)

    def test_fill_delivery_place(self, driver):
        with pytest.allure.step('Fill delivery place'):
            tests.fill_in_delivery_place(driver)

    def test_select_territory(self, driver):
        with pytest.allure.step('select territory'):
            tests.select_territory(driver)

    def test_select_location(self, driver):
        with pytest.allure.step('select location'):
            tests.select_location(driver)

    def test_fill_vendor_po_box(self, driver):
        with pytest.allure.step('Fill vendor po box'):
            tests.fill_in_vendor_po_box(driver)

    def test_fill_vendor_city(self, driver):
        with pytest.allure.step('Fill vendor city'):
            tests.fill_in_vendor_city(driver)

    def test_fill_vendor_state(self, driver):
        with pytest.allure.step('fill vendor state'):
            tests.fill_in_vendor_state(driver)

    def test_fill_vendor_post_code(self, driver):
        with pytest.allure.step('Fill vendor post code'):
            tests.fill_in_vendor_post_code(driver)

    def test_fill_vendor_country(self, driver):
        with pytest.allure.step('dill vendor country'):
            tests.fill_in_vendor_country(driver)

    def test_fill_shipping_po_box(self, driver):
        with pytest.allure.step('fill shipping po box'):
            tests.fill_in_shipping_po_box(driver)

    def test_fill_shipping_city(self, driver):
        with pytest.allure.step('fill shipping city'):
            tests.fill_in_shipping_city(driver)

    def test_fill_shipping_state(self, driver):
        with pytest.allure.step('fill shipping state'):
            tests.fill_in_shipping_state(driver)

    def test_fill_shipping_post_code(self, driver):
        with pytest.allure.step('fill shipping post code'):
            tests.fill_in_shipping_post_code(driver)

    def test_fill_shipping_country(self, driver):
        with pytest.allure.step('Fill shipping country'):
            tests.fill_in_shipping_country(driver)

    # def test_fill_description(self, driver):
    #     tests.fill_in_description(driver)

    def test_add_product(self, driver):
        with pytest.allure.step('Add product'):
            tests.add_product(driver)

    def test_save_po(self, driver):
        with pytest.allure.step('save PO'):
            tests.save_po(driver)

    #
    # def test_close_alert(self, driver):
    #     tests.close_alert(driver)

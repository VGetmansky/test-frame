import pytest
from crm.tests import products_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With Products list')
@pytest.mark.test
class TestWorkWithProductList:
    def test_click_category_all(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_product_category(self, driver, url):
        with pytest.allure.step('Select all'):
            tests.select_products_category(driver, url)


@pytest.allure.testcase('Work With Product Profile')
@pytest.mark.test
class TestClickAddProductButton:
    def test_click_add_button(self, driver, url):
        with pytest.allure.step('Click add Product'):
            tests.click_add_product(driver, url)


@pytest.allure.testcase('Work With Product Profile')
@pytest.mark.test
class TestFillProductProfile:
    def test_fill_part_number(self, driver):
        with pytest.allure.step('Fill Part Number'):
            tests.fill_part_number(driver)

    def test_fill_nsn_number(self, driver):
        with pytest.allure.step('Fill NSN Number'):
            tests.fill_nsn_number(driver)

    def test_fill_manufacturer(self, driver):
        with pytest.allure.step('Fill Manufacturer'):
            tests.fill_in_manufacturer_field(driver)

    def test_fill_support_start_date(self, driver):
        with pytest.allure.step('Fill Support start date'):
            tests.select_support_start_date(driver)

    def test_select_sales_start_date(self, driver):
        with pytest.allure.step('Fill sales start date'):
            tests.select_sales_start_date(driver)

    def test_fill_support_expiry_date(self, driver):
        with pytest.allure.step('Fill Support start date'):
            tests.select_support_expiry_date(driver)

    def test_select_sales_end_date(self, driver):
        with pytest.allure.step('Fill sales end date'):
            tests.select_sales_end_date(driver)

    def test_fill_website(self, driver):
        with pytest.allure.step('Fill Website'):
            tests.fill_website(driver)

    def test_fill_vendor(self, driver):
        with pytest.allure.step('Fill Vendor'):
            tests.fill_in_vendor_name(driver)

    def test_fill_vendor_partno(self, driver):
        with pytest.allure.step('Fill sales end date'):
            tests.fill_vendor_partno(driver)

    def test_fill_product_sheet(self, driver):
        with pytest.allure.step('Fill Product Sheet'):
            tests.fill_product_sheet(driver)

    def test_fill_mfr_part_number(self, driver):
        with pytest.allure.step('Fill MFR Part Number'):
            tests.fill_mfr_partno(driver)

    def test_fill_serial_number(self, driver):
        with pytest.allure.step('Fill Serial Number'):
            tests.fill_seriall_no(driver)

    def test_check_vat_percent(self, driver):
        with pytest.allure.step('Check VAT Percent'):
            tests.check_vat_percent(driver)

    def test_check_service_percent(self, driver):
        with pytest.allure.step('Check Service Percent'):
            tests.check_service_percent(driver)

    def test_check_tax_non_percent(self, driver):
        with pytest.allure.step('Check Tax NON Percent'):
            tests.check_tax_non_percent(driver)

    def test_check_sales(self, driver):
        with pytest.allure.step('Check Tax for shipping'):
            tests.check_sales(driver)

    def test_check_tax_for_shipping(self, driver):
        with pytest.allure.step('Check Tax for shipping'):
            tests.check_tax_for_shipping(driver)
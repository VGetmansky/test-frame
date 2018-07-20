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
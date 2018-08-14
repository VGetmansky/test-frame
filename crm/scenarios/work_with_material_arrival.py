import pytest
from crm.tests import material_arrival_tests as tests
from crm.scenarios.login_scenario import TestLogInApp

TestLogInApp()


@pytest.allure.testcase('Work With Material Arrival')
@pytest.mark.test
class TestWorkWithMaterialArrival:
    def test_click_category_all(self, driver):
        with pytest.allure.step('Select all'):
            tests.click_all_category(driver)

    def test_click_Material_arrival(self, driver, url):
        with pytest.allure.step('Select Material Arrival'):
            tests.select_material_arrival_category(driver, url)
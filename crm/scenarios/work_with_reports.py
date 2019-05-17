import pytest
from crm.tests import reports_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With RFQ')
@pytest.mark.test
class TestWorkWithRFQList:
    def test_open_quotes_tab(self, driver):
        with pytest.allure.step('Select quote'):
            tests.select_quote(driver)

    def test_open_quotes_details(self, driver, url):
        with pytest.allure.step('Open quotes details'):
            tests.open_quote_details(driver, url)

    def test_expand_pdfmaker_tab(self, driver):
        with pytest.allure.step('Expand PDF maker'):
            tests.expand_pdfmaker(driver)

    def test_click_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    # def test_get_body_data(self, driver):
    #     with pytest.allure.step('Get body data'):
    #         tests.get_body_data(driver)

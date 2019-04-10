import pytest
from crm.tests import reports_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With RFQ')
@pytest.mark.test
class TestWorkWithRFQList:
    def test_open_invoice_tab(self, driver):
        with pytest.allure.step('Select invoice'):
            tests.select_quote(driver)

    def test_open_quotes_details(self, driver, url):
        with pytest.allure.step('Open quotes details'):
            tests.open_quote_details(driver, url)

    def test_expand_pdfmaker_tab(self, driver):
        with pytest.allure.step('Expand PDF maker'):
            tests.expand_pdfmaker(driver)

    def test_select_rfq(self, driver):
        with pytest.allure.step('work with'):
            tests.select_rfq(driver)
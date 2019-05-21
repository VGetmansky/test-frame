import pytest
from crm.tests import reports_tests as tests
from crm.scenarios.login_scenario import TestLogInApp
from crm.scenarios import parse_pdf as parse

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

    def test_parse_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path)

    # def test_get_body_data(self, driver):
    #     with pytest.allure.step('Get body data'):
    #         tests.get_body_data(driver)

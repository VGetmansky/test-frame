import pytest
from crm.tests import documents_test as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.mark.test
class TestWorkWithSOList:
    def test_open_documents_tab(self, driver):
        tests.select_documents(driver)
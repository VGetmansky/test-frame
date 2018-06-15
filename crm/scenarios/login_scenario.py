import pytest
from crm.tests import login_tests
import allure


@pytest.allure.testcase('login')
@pytest.mark.test
class TestLogInApp:
    def test_open_url(self, driver, url):
        with pytest.allure.step('Open URL'):
                login_tests.open_url(driver, url)

    def test_add_credentials(self, driver, username, password):
        with pytest.allure.step('Add cridentials'):
            login_tests.add_credentials(driver, username, password)

    def test_submit_form(self, driver):
        with pytest.allure.step('Submit Form'):
            login_tests.submit_form(driver)

    def test_verify_url(self, driver, url):
        with pytest.allure.step('Verify URL'):
            login_tests.verify_url(driver, url)


@pytest.mark.test
class TestLogOutApp:
    def test_logout(self, driver):
        login_tests.logout(driver)

    def test_verify_logout(self, driver):
        login_tests.verify_logout(driver)

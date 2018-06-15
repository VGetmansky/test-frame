import pytest
from portal.tests import login_tests


@pytest.mark.test
class TestLogInApp:
    def test_open_url(self, driver, url):
        login_tests.open_url(driver, url)

    def test_open_login_form(self, driver):
        login_tests.open_login_form(driver)

    def test_add_credentials(self, driver, username, password):
        login_tests.add_credentials(driver, username, password)

    def test_submit_form(self, driver):
        login_tests.submit_form(driver)

    def test_verify_url(self, driver, url):
        login_tests.verify_url(driver, url)


@pytest.mark.test
class TestMainNavigation:
    def test_open_quotes(self, driver, url):
        login_tests.open_quotes_tab(driver,url)

    def test_open_orders(self, driver, url):
        login_tests.open_orders_tab(driver, url)

    def test_open_profile(self, driver, url):\
        login_tests.open_profile_tab(driver, url)
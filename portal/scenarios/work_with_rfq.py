import pytest
from portal.tests import login_tests
from portal.scenarios.login_scenario import TestLogInApp

TestLogInApp()


@pytest.mark.test
class TestRfqCreation:
    def test_new_rfq(self, driver):
        login_tests.new_rfq(driver)

    def test_new_rfq(self, driver):
        login_tests.new_rfq(driver)

    def test_rfq_step_one(self, driver):
        login_tests.fill_step_one(driver)

    def test_rfq_step_two(self, driver):
        login_tests.fill_step_two(driver)

    def test_rfq_step_three(self, driver):
        login_tests.fill_step_three(driver)
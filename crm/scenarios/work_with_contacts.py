import pytest
from crm.tests import contacts_tests as tests
from crm.scenarios.login_scenario import TestLogInApp


TestLogInApp()


@pytest.allure.testcase('Work With Contacts')
@pytest.mark.test
class TestWorkWithContactsList:
    def test_open_contacts_tab(self, driver):
        with pytest.allure.step('Select Contacts'):
            tests.select_contacts(driver)


@pytest.mark.test
class TestClickAddContactsButton:
    def test_click_add_contact_button(self, driver, url):
        with pytest.allure.step('Click add Contact'):
            tests.click_add_contact(driver, url)

    def test_select_contact_acounts_name(self, driver):
        with pytest.allure.step('Select Accounts name'):
            tests.fill_in_accounts_name(driver)

    def test_fill_contact_first_name(self, driver):
        with pytest.allure.step('Fill First Name'):
            tests.fill_contact_first_name(driver)

    def test_select_contact_location_name(self, driver):
        with pytest.allure.step('Select Location name'):
            tests.fill_contact_last_name(driver)

    def test_select_contact_relationships(self, driver):
        with pytest.allure.step('Select relationship'):
            tests.fill_in_relationships(driver)

    def test_fill_contact_last_name(self, driver):
        with pytest.allure.step('Fill Last Name'):
            tests.fill_contact_last_name(driver)

    def test_select_contact_reports_to(self, driver):
        with pytest.allure.step('Select Reports To'):
            tests.fill_in_reports_to(driver)

    def test_fill_contact_title(self, driver):
        with pytest.allure.step('Fill Contact Title'):
            tests.fill_contact_title(driver)

    def test_fill_contact_department(self, driver):
        with pytest.allure.step('Fill Contact Department'):
            tests.fill_contact_department(driver)

    def test_fill_primary_email(self, driver):
        with pytest.allure.step('Fill Primary Email'):
            tests.fill_contact_primary_email(driver)

    def test_click_fill_contact_assistant(self, driver):
        with pytest.allure.step('Fill Contact Assistant'):
            tests.fill_contact_assistant(driver)

    def test_fill_contact_assistant_phone(self, driver):
        with pytest.allure.step('Fill Contact Assistant Phone'):
            tests.fill_contact_assistant_phone(driver)

    def test_check_email_opt_out_checkbox(self, driver):
        with pytest.allure.step('Check Email Opt Out'):
            tests.check_email_opt_out(driver)

    def test_check_reference(self, driver):
        with pytest.allure.step('Check Reference'):
            tests.check_reference(driver)

    def test_check_notify_owner(self, driver):
        with pytest.allure.step('Check Notify Owner'):
            tests.check_notify_owner(driver)

    def test_fill_role(self, driver):
        with pytest.allure.step('Fill Role'):
            tests.fill_contact_role(driver)

    def test_fill_contact_id(self, driver):
        with pytest.allure.step('Fill Role'):
            tests.fill_contact_id(driver)

    def test_click_office_phone(self, driver):
        with pytest.allure.step('Fill office phone'):
            tests.fill_office_phone(driver)

    def test_fill_mobile_phone(self, driver):
        with pytest.allure.step('Fill Mobile Phone'):
            tests.fill_contact_mobile_phone(driver)

    def test_select_lead_source(self, driver):
        with pytest.allure.step('Select Lead Source'):
            tests.select_lead_source(driver)

    def test_fill_home_phone(self, driver):
        with pytest.allure.step('Fill Home Phone'):
            tests.fill_contact_home_phone(driver)

    def test_fill_secondary_phone(self, driver):
        with pytest.allure.step('Fill Secondary Phone'):
            tests.fill_contact_secondary_phone(driver)

    def test_fill_contact_fax(self, driver):
        with pytest.allure.step('Fill Fax'):
            tests.fill_contact_fax(driver)

    def test_fill_secondary_email(self, driver):
        with pytest.allure.step('Fill Secondary Email'):
            tests.fill_contact_secondary_email(driver)

    def test_check_do_not_call_checkbox(self, driver):
        with pytest.allure.step('Check Do Not Call'):
            tests.check_do_not_call(driver)

    def test_check_sync_to_qb_checkbox(self, driver):
        with pytest.allure.step('Check Sync To QA'):
            tests.check_sync_to_qb(driver)

    def test_check_sent_to_qb_checkbox(self, driver):
        with pytest.allure.step('Check Sent To QA'):
            tests.check_seny_to_qb(driver)

    def test_check_portal_user_checkbox(self, driver):
        with pytest.allure.step('Check Portal User'):
            tests.check_portal_user_checkbox(driver)

    def test_fill_mailing_street(self, driver):
        with pytest.allure.step('Fill Mailing Street'):
            tests.fill_contact_mailing_street(driver)

    def test_fill_mailing_po_box(self, driver):
        with pytest.allure.step('Fill Mailing PO Box'):
            tests.fill_contact_mailing_po_box(driver)

    def test_fill_mailing_city(self, driver):
        with pytest.allure.step('Fill Mailing City'):
            tests.fill_contact_mailing_city(driver)

    def test_fill_mailing_state(self, driver):
        with pytest.allure.step('Fill Mailing State'):
            tests.fill_contact_mailing_state(driver)

    def test_fill_mailing_zip(self, driver):
        with pytest.allure.step('Fill Mailing ZIP'):
            tests.fill_contact_mailing_zip(driver)

    def test_fill_mailing_country(self, driver):
        with pytest.allure.step('Fill Mailing Country'):
            tests.fill_contact_mailing_country(driver)

    def test_fill_other_street(self, driver):
        with pytest.allure.step('Fill Other Street'):
            tests.fill_contact_other_street(driver)

    def test_fill_other_po_box(self, driver):
        with pytest.allure.step('Fill Other PO Box'):
            tests.fill_contact_other_po_box(driver)

    def test_fill_other_city(self, driver):
        with pytest.allure.step('Fill Other City'):
            tests.fill_contact_other_city(driver)

    def test_fill_other_state(self, driver):
        with pytest.allure.step('Fill Other State'):
            tests.fill_contact_other_state(driver)

    def test_fill_other_zip(self, driver):
        with pytest.allure.step('Fill Other ZIP'):
            tests.fill_contact_other_zip(driver)

    def test_fill_other_country(self, driver):
        with pytest.allure.step('Fill Other Country'):
            tests.fill_contact_other_country(driver)

    def test_fill_description(self, driver):
        with pytest.allure.step('Fill Description'):
            tests.fill_description(driver)

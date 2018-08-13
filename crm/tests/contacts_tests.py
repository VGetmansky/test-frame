from crm.data import authorization_data as auth_data, contacts_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def select_contacts(driver):
    if driver.title != "Contacts":
        additional.wait_element_for_click(driver, auth_data.contacts_main_button_id)
    assert "Contacts", driver.title


def click_add_contact(driver, url):
    additional.wait_element(driver, data.add_contact_id, 'id')
    driver.find_element(By.ID, data.add_contact_id).click()
    time.sleep(5)
    assert (url + data.expected_url) == driver.current_url and ("Contacts", driver.title)


# def fill_in_vendor_field(driver):
#     element_id = data.vendor_list_id
#     additional.select_first_cell(driver, element_id, False)


# ------------------ Basic Information ------------------


def fill_contact_first_name(driver):
    value = data.contact_first_name_id
    text = "Autotest ContactName"
    additional.fill_text_field(driver, value, text)


def fill_contact_last_name(driver):
    value = data.contact_last_name_id
    text = "Autotest ContactLastName"
    additional.fill_text_field(driver, value, text)


def fill_in_accounts_name(driver):
    element_id = data.contact_account_name_id
    additional.wait_element(driver, data.contact_account_name_id, 'id')
    additional.select_first_cell(driver, element_id, True)


def select_locations(driver):
    element_id = data.contact_locations_id
    additional.wait_element(driver, data.contact_locations_id, 'id')
    additional.select_first_cell(driver, element_id, False)


def select_lead_source(driver):
    value = data.lead_source_id
    text = data.default_dropdown_value
    # additional.select_value_from_dropdown(driver, value, text)
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def fill_contact_title(driver):
    value = data.title_id
    text = "Autotest Title"
    additional.fill_text_field(driver, value, text)


def fill_contact_department(driver):
    value = data.department_id
    text = "Autotest Department"
    additional.fill_text_field(driver, value, text)


def fill_contact_primary_email(driver):
    value = data.primary_email_id
    text = "testemail@testmail.ccc"
    additional.fill_text_field(driver, value, text)


def fill_contact_assistant(driver):
    value = data.assistant_id
    text = "Assistance name"
    additional.fill_text_field(driver, value, text)


def fill_contact_assistant_phone(driver):
    value = data.assistant_phone_id
    text = "Assistance phone"
    additional.fill_text_field(driver, value, text)


def check_email_opt_out(driver):
    value = data.email_opt_out_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_reference(driver):
    value = data.reference_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_notify_owner(driver):
    value = data.notify_owner_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def fill_contact_role(driver):
    value = data.contact_role_id
    text = "Test Role"
    additional.fill_text_field(driver, value, text)


def fill_contact_id(driver):
    value = data.contact_id_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_office_phone(driver):
    value = data.office_phone_id
    text = "11111111111111111111"
    additional.fill_text_field(driver, value, text)


def fill_contact_mobile_phone(driver):
    value = data.mobile_phone_id
    text = "11111111111111111"
    additional.fill_text_field(driver, value, text)


def fill_in_relationships(driver):
    element_id = data.relationships_id
    additional.wait_element(driver, data.relationships_id, 'id')
    additional.select_first_cell(driver, element_id, False)


def fill_contact_home_phone(driver):
    value = data.home_phone_id
    text = "11111111111111"
    additional.fill_text_field(driver, value, text)


def fill_contact_secondary_phone(driver):
    value = data.secondary_phone_id
    text = "11111111111111"
    additional.fill_text_field(driver, value, text)


def fill_contact_fax(driver):
    value = data.fax_id
    text = "11111111111"
    additional.fill_text_field(driver, value, text)


def select_date_of_birth(driver):
    value = data.date_birth_id
    date = '01-04-1980'
    additional.select_calendar_date(driver, value, date)


def fill_in_reports_to(driver):
    element_id = data.reports_to_id
    additional.wait_element(driver, data.reports_to_id, 'id')
    additional.select_first_cell(driver, element_id, False)


def fill_contact_secondary_email(driver):
    value = data.secondary_email_id
    text = "Test Contact ID"
    additional.fill_text_field(driver, value, text)


def check_do_not_call(driver):
    value = data.do_not_call_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def fill_in_order_approval_limit(driver):
    element_id = data.order_approval_limit_id
    additional.wait_element(driver, data.order_approval_limit_id, 'id')
    additional.select_first_cell(driver, element_id, False)


# ------------------ Custom Information ------------------


def check_sync_to_qb(driver):
    value = data.sync_to_qb_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_seny_to_qb(driver):
    value = data.sent_to_qb_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def select_qb_customer_type(driver):
    value = data.qb_customer_type_id
    text = data.default_dropdown_value
    # additional.select_value_from_dropdown(driver, value, text)
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def select_qb_company(driver):
    value = data.lead_source_id
    text = data.default_dropdown_value
    # additional.select_value_from_dropdown(driver, value, text)
    additional.select_element_with_text_from_list(driver, value, 'id', text)


# ------------------ Customer Portal Details ------------------


def check_portal_user_checkbox(driver):
    value = data.portal_user_checkbox_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def select_support_start_date(driver):
    value = data.support_start_date_id
    date = '01-04-1980'
    additional.select_calendar_date(driver, value, date)


def select_support_end_date(driver):
    value = data.support_end_date_id
    date = '31-12-2020'
    additional.select_calendar_date(driver, value, date)


# ------------------ Address Details ------------------


def fill_contact_mailing_street(driver):
    value = data.mailing_street_id
    text = "Test Mailing Street"
    additional.fill_text_field(driver, value, text)


def fill_contact_mailing_po_box(driver):
    value = data.mailing_po_box_id
    text = "Test Mailing PO Box"
    additional.fill_text_field(driver, value, text)


def fill_contact_mailing_city(driver):
    value = data.mailing_city_id
    text = "Test Mailing city"
    additional.fill_text_field(driver, value, text)


def fill_contact_mailing_state(driver):
    value = data.mailing_state_id
    text = "Test Mailing State"
    additional.fill_text_field(driver, value, text)


def fill_contact_mailing_zip(driver):
    value = data.mailing_zip_id
    text = "Test Mailing_ZIP"
    additional.fill_text_field(driver, value, text)


def fill_contact_mailing_country(driver):
    value = data.mailing_country_id
    text = "Test Mailing Country"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_street(driver):
    value = data.other_street_id
    text = "Test Other Street"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_po_box(driver):
    value = data.other_box_id
    text = "Test Other PO Box"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_city(driver):
    value = data.other_city_id
    text = "Test Other city"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_state(driver):
    value = data.other_state_id
    text = "Test Other State"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_zip(driver):
    value = data.other_zip_id
    text = "Test Other_ZIP"
    additional.fill_text_field(driver, value, text)


def fill_contact_other_country(driver):
    value = data.other_country_id
    text = "Test Other Country"
    additional.fill_text_field(driver, value, text)

# ------------------ Description Details ------------------


def fill_description(driver):
    value = data.description_id
    text = "Autotest Created Contact"
    additional.fill_text_field(driver, value, text)


# ------------------ Profile Picture ------------------
#
#
# def click_save_account(driver):
#     driver.execute_script("window.scrollTo(0, 0)")
#     value = data.save_button
#     text = "Save"
#     additional.select_element_with_text_from_list(driver, value, 'xpath', text)

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
    assert (url + data.expected_url) == driver.current_url and ("Contacts", driver.title)


# def fill_in_vendor_field(driver):
#     element_id = data.vendor_list_id
#     additional.select_first_cell(driver, element_id, False)


def fill_contact_first_name(driver):
    value = data.contact_first_name_id
    text = "Autotest ContactName"
    additional.fill_text_field(driver, value, text)


def fill_contact_last_name(driver):
    value = data.contact_last_name_id
    text = "Autotest ContactLastName"
    additional.fill_text_field(driver, value, text)


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


def fill_contact_role(driver):
    value = data.contact_role_id
    text = "Test Role"
    additional.fill_text_field(driver, value, text)


def fill_contact_id(driver):
    value = data.contact_id_id
    text = "Test Contact ID"
    additional.fill_text_field(driver, value, text)


def fill_office_phone(driver):
    value = data.office_phone_id
    text = "11111111111111111111"
    additional.fill_text_field(driver, value, text)


def fill_contact_mobile_phone(driver):
    value = data.mobile_phone_id
    text = "11111111111111111"
    additional.fill_text_field(driver, value, text)


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


def fill_contact_secondary_email(driver):
    value = data.secondary_email_id
    text = "Test Contact ID"
    additional.fill_text_field(driver, value, text)

# def fill_in_member_of(driver):
#     element_id = data.member_of_id
#     additional.select_first_cell(driver, element_id, False)
#     #additional.wait_element(driver, data.overwrite_dialog_no, 'xpath')
#     time.sleep(2)
#     additional.select_element_with_text_from_list(driver, data.overwrite_dialog_no, "xpath", "No")

#
#
# def select_industry(driver):
#     value = data.industry_id
#     text = data.default_dropdown_value
#     additional.select_value_from_dropdown(driver, value, text)

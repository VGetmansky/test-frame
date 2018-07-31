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

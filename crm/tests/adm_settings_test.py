from crm.data import authorization_data as auth_data, adm_settings_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def click_settings(driver):
    additional.wait_element(driver, data.settings_button_id, 'id')
    additional.click_element_by_id(driver, data.settings_button_id)


def select_crm_settings(driver):
    additional.select_element_with_text_from_list(driver, data.crm_settings_id, 'id', 'CRM Settings')


def select_studio_category(driver):
    additional.wait_element(driver, data.studio, 'xpath')
    additional.click_element_by_xpath(driver, data.studio)


def select_edit_fields(driver):
    additional.wait_element(driver, data.edit_fields, 'xpath')
    additional.click_element_by_xpath(driver, data.edit_fields)


def click_opportunities(driver):
    time.sleep(3)
    additional.wait_element(driver, data.opportunities, 'xpath')
    additional.select_element_with_text_from_list(driver, data.opportunities, 'xpath', 'Opportunities')
    # additional.click_element_by_xpath(driver, data.opportunities)
    #additional.wait_element_for_click(driver, data.opportunities)


def click_contacts(driver):
    time.sleep(3)
    additional.wait_element(driver, data.contacts, 'xpath')
    additional.select_element_with_text_from_list(driver, data.contacts, 'xpath', 'Contacts')
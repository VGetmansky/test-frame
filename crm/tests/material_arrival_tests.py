from crm.data import authorization_data as auth_data, material_arrival_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def click_all_category(driver):
    additional.select_category_all(driver)


def select_material_arrival_category(driver, url):
    additional.wait_element(driver, data.material_arrival_id, 'id')
    # driver.find_element(By.ID, data.material_arrival_id).click()
    driver.find_elements(By.ID, data.material_arrival_id)[1].click()
    assert (url + data.material_arrival_expected_url) == driver.current_url and ("WHStock", driver.title)


def select_vendor(driver):
    value = data.vendor_select_id
    text = data.autotest_vendor
    additional.select_value_from_dropdown(driver, value, text)


def filter_by_last_po(driver):
    value = data.po_filter_id
    additional.select_last_element_from_list(driver, value)


def check_po_checkboxes(driver):
    value = data.po_checkboxes
    additional.check_all_item_checkbuttonspo(driver, value)


def select_shipping_notice_category(driver, url):
    additional.wait_element(driver, data.shipping_notice_id, 'id')
    driver.find_elements(By.ID, data.shipping_notice_id)[1].click()
    assert (url + data.shipping_notice_expected_url) == driver.current_url and ("WHStock", driver.title)


def select_account(driver):
    value = data.select_account_id
    text = data.autotest_account
    additional.select_value_from_dropdown(driver, value, text)


def filter_by_last_so(driver):
    value = data.so_filter_id
    additional.select_last_element_from_list(driver, value)
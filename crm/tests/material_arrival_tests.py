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
    value = data.material_arrival_checkboxes
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
    additional.wait_element(driver, value, 'id')
    additional.select_last_element_from_list(driver, value)


def filter_add_note(driver):
    value = data.notes_id
    text = "Autotest Filled Notes"
    additional.fill_text_field(driver, value, text)


def check_shipping_notice_so_checkboxes(driver):
    value = data.material_arrival_checkboxes
    additional.check_all_item_checkbuttonspo(driver, value)


def select_inspection_category(driver, url):
    additional.wait_element(driver, data.inspection_id, 'id')
    driver.find_elements(By.ID, data.inspection_id)[1].click()
    assert (url + data.inspection_expected_url) == driver.current_url and ("WHStock", driver.title)


def filter_by_last_inspection(driver, page):
    value = data.inspection_select_id
    additional.select_last_material_arrival_inspection(driver, value, page)


def select_all_material_arrival_inspection(driver):
    value = data.select_all_button_id
    driver.find_element(By.ID, value).click()
    driver.find_element(By.ID, value).click()


def select_receiving(driver, url):
    additional.wait_element(driver, data.receiving_id, 'id')
    driver.find_elements(By.ID, data.receiving_id)[1].click()
    assert (url + data.receiving_expected_url) == driver.current_url and ("WHStock", driver.title)


def select_all_material_arrival_chkboxes(driver):
    value = data.select_all_button_id
    driver.find_element(By.ID, value).click()


def select_packing(driver, url):
    additional.wait_element(driver, data.packing_id, 'id')
    driver.find_elements(By.ID, data.packing_id)[1].click()
    assert (url + data.receiving_expected_url) == driver.current_url and ("WHStock", driver.title)


def fill_material_arrival_warehouse_index(driver):
    text = "2"
    value = data.isle_id
    additional.fill_text_field(driver, value, text)
    value = data.shelf_id
    additional.fill_text_field(driver, value, text)
    value = data.holder_id
    additional.fill_text_field(driver, value, text)


def click_material_arrival_deliver(driver):
    additional.click_material_arrival_buttons(driver, data.deliver_button)


def click_material_arrival_send_notice(driver):
    additional.click_material_arrival_buttons(driver, data.send_notice_button)


def click_material_arrival_approve(driver):
    additional.click_material_arrival_buttons(driver, data.approve_button)


def click_material_arrival_receive(driver):
    additional.click_material_arrival_buttons(driver, data.receive_button)
from crm.data import authorization_data as auth_data, products_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def click_all_category(driver):
    additional.select_category_all(driver)


def select_products_category(driver, url):
    additional.wait_element(driver, data.products_category_id, 'id')
    driver.find_element(By.ID, data.products_category_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Products", driver.title)


def click_add_product(driver, url):
    additional.wait_element(driver, data.add_product_id, 'id')
    driver.find_element(By.ID, data.add_product_id).click()
    assert (url + data.expected_product_url) == driver.current_url


def select_support_start_date(driver):
    value = data.support_start_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def select_support_expiry_date(driver):
    value = data.suppport_expiry_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def fill_part_number(driver):
    value = data.part_number_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def fill_nsn_number(driver):
    value = data.nsn_number_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_in_manufacturer_field(driver):
    element_id = data.search_manufacturer_id
    additional.select_first_cell(driver, element_id, False)


def fill_website(driver):
    value = data.website_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def fill_mfr_partno(driver):
    value = data.mfr_partno_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_seriall_no(driver):
    value = data.serial_no_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def select_sales_start_date(driver):
    value = data.sales_start_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def select_sales_end_date(driver):
    value = data.sales_end_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def fill_in_vendor_name(driver):
    element_id = data.vendor_name_id
    additional.select_first_cell(driver, element_id, False)


def fill_vendor_partno(driver):
    value = data.vendor_parnno_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def fill_product_sheet(driver):
    value = data.product_sheet_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_vendor_partno_no(driver):
    value = data.vendor_parnno_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def fill_product_sheet(driver):
    value = data.product_sheet_id
    text = "PN1"
    additional.fill_text_field(driver, value, text)


def check_vat_percent(driver):
    value = data.vat_percent_tax_check_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_service_percent(driver):
    value = data.service_percent_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_tax_non_percent(driver):
    value = data.tax_non_percent_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_sales(driver):
    value = data.saves_percent_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_tax_for_shipping(driver):
    value = data.tax_for_shipping_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)
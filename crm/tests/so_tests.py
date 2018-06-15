from crm.data import so_data as data, authorization_data as auth_data
from selenium.webdriver.common.by import By
import common_functions as additional
import datetime


def click_edit_so(driver, value):
    driver.find_element(By.ID, value).click()


def select_sales_orders(driver):
    if driver.title != "Sales Order":
        driver.find_element(By.ID, auth_data.so_main_button_id).click()
    assert ("Sales Order", driver.title)


def click_add_so(driver, url):
    driver.find_element(By.ID, data.add_so_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Sales Orders", driver.title)


def fill_in_account_field(driver):
    element_id = data.account_selector_id
    additional.select_first_cell(driver, element_id, True)


def fill_in_billing_address(driver):
    field = data.billing_address_id
    text = "Test billing address"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_address(driver):
    field = data.shipping_address_id
    text = "Test Shipping Address"
    additional.fill_text_field(driver, field, text)


def fill_in_client_po(driver):
    clientpoid = data.client_po_id
    text = "Autotest_Client_PO_" + str(datetime.datetime.now())
    additional.fill_text_field(driver, clientpoid, text)


def add_product(driver):
    element_id = data.product_list_button
    additional.select_first_cell(driver, element_id, False)


def save_so(driver):
    driver.find_element(By.ID, data.save_so_button_id).click()


def close_alert(driver):
    driver.find_element(By.XPATH, auth_data.home).click()
    driver.switch_to.alert.accept()
    assert("Home", driver.title)


# text fields
def fill_in_billing_po_box(driver):
    field = data.billing_po_box_id
    text = "Test BillingPOID"
    additional.fill_text_field(driver, field, text)


def fill_in_billing_city(driver):
    field = data.billing_city_id
    text = "Test BillingCity ID"
    additional.fill_text_field(driver, field, text)


def fill_in_billing_state(driver):
    field = data.billing_state_id
    text = "Test BillingState"
    additional.fill_text_field(driver, field, text)


def fill_in_billing_post_code(driver):
    field = data.billing_post_code_id
    text = "Test Billing Post Code"
    additional.fill_text_field(driver, field, text)


def fill_in_billing_country(driver):
    field = data.billing_country_id
    text = "Test Billing Country"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_po_box(driver):
    field = data.shipping_po_box_id
    text = "Test ShippingPOID"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_city(driver):
    field = data.shipping_city_id
    text = "Test ShippingCity ID"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_state(driver):
    field = data.shipping_state_id
    text = "Test ShippingState"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_post_code(driver):
    field = data.shipping_post_code_id
    text = "Test Shipping Post Code"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_country(driver):
    field = data.shipping_country_id
    text = "Test Shipping Country"
    additional.fill_text_field(driver, field, text)



from selenium.webdriver.common.by import By
from crm.data import quotes_data as data, authorization_data as auth_data
import common_functions as additional


def select_quote(driver):
    if driver.title != "Quotes":
        driver.find_element(By.ID, auth_data.quotes_main_button_id).click()
    assert "Quotes", driver.title


def click_add_quote(driver, url):
    driver.find_element(By.ID, data.add_quote_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Quotes", driver.title)


def fill_in_account_field(driver):
    element_id = data.account_selector_id
    additional.select_first_cell(driver, element_id, True)


def fill_in_cust_ref(driver):
    field = data.cust_ref_id
    text = "Autotest Cust ref: 1245"
    additional.fill_text_field(driver, field, text)


def fill_in_billing_address(driver):
    billingid = data.billing_address_id
    text = "Test billing address"
    additional.fill_text_field(driver, billingid, text)


def fill_in_shipping_address(driver):
    shippingid = data.shipping_address_id
    text = "Test Shipping Address"
    additional.fill_text_field(driver, shippingid, text)


def fill_in_place_of_delivery(driver):
    field = data.place_of_delivery_id
    text = "Test delivery location"
    additional.fill_text_field(driver, field, text)


def select_quote_status(driver):
    value = data.quote_stage_id
    text = data.quote_stage
    additional.select_value_from_dropdown(driver, value, text)


def select_proirity(driver):
    value = data.priority_id
    text = data.priority
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_id
    text = data.terms_of_delivery
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_sale(driver):
    value = data.terms_of_sale_id
    text = data.terms_of_sale
    additional.select_value_from_dropdown(driver, value, text)


def add_product(driver):
    element_id = data.product_list_button
    additional.select_first_cell(driver, element_id, False)


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


def fill_in_description_details(driver):
    field = data.quote_description_details_id
    text = "Autotest created description"
    additional.fill_text_field(driver, field, text)


def save_so(driver):
    driver.find_element(By.ID, data.save_quote_button_id).click()


def close_alert(driver):
    driver.find_element(By.XPATH, auth_data.home).click()
    driver.switch_to.alert.accept()
    assert("Home", driver.title)
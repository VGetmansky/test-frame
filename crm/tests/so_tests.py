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
    value = data.account_selector_id
    additional.wait_element(driver, value, 'id')
    additional.select_first_cell(driver, value, True)


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

#   ------------------------------------------


def select_contact_name(driver):
    value = data.contact_name_selector_id
    additional.select_first_cell(driver, value, False)
    additional.wait_element(driver, data.contact_name_overwrite_adress, "xpath")
    driver.find_elements(By.XPATH, data.contact_name_overwrite_adress)[
        len(driver.find_elements(By.XPATH, data.contact_name_overwrite_adress)) - 1].click()


def select_customer_quote(driver):
    value = data.customer_quote_id
    additional.select_first_cell(driver, value, False)


def select_location(driver):
    value = data.location_selector_id
    additional.select_first_cell(driver, value, False)


def select_aircraft(driver):
    value = data.aircraft_id
    additional.select_first_cell(driver, value, False)


def select_assets(driver):
    value = data.assets_id
    additional.select_first_cell(driver, value, False)


def select_sold_by(driver):
    value = data.sold_by_id
    additional.wait_element(driver, value, 'id')
    additional.select_first_cell(driver, value, False)


def select_status(driver):
    value = data.status_selector_id
    text = data.status_approved_value
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_payment(driver):
    value = data.terms_of_payment_id
    text = data.terms_of_payment_value
    additional.select_value_from_dropdown(driver, value, text)


def select_priority(driver):
    value = data.priority_id
    text = data.priority_value
    additional.select_value_from_dropdown(driver, value, text)


def select_ship_via(driver):
    value = data.ship_via_selector_id
    text = data.ship_via_value
    additional.select_value_from_dropdown(driver, value, text)


def select_assigned_to(driver):
    value = data.assigned_to_selector_id
    text = data.assigned_to_value
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_selector_id
    text = data.terms_of_delivery_value
    additional.select_value_from_dropdown(driver, value, text)


def select_territory(driver):
    value = data.territory_selector_id
    text = data.territory_value
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_sales_commission(driver):
    value = data.sales_commission_id
    text = "2"
    additional.fill_text_field(driver, value, text)


def fill_in_account_number(driver):
    value = data.account_num_id
    text = "221"
    additional.fill_text_field(driver, value, text)


def fill_in_place_of_delivery(driver):
    value = data.place_of_delivery_id
    text = "Autotest Place of Delivery"
    additional.fill_text_field(driver, value, text)

#   ------------------------------------------


def add_product(driver):
    value = data.product_list_button
    additional.wait_element(driver, data.part_number_field_id, 'id')  #  additional.wait_element(driver, value, 'id')
    additional.select_first_cell(driver, value, False)


def save_so(driver):
    driver.execute_script("window.scrollTo(0, 0)")
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


def fill_in_so_notes(driver):
    field = data.notes_id
    text = "Test Note"
    additional.fill_text_field(driver, field, text)



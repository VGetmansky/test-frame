from crm.data import invoice_data as data, authorization_data as auth_data, values_data as values
from selenium.webdriver.common.by import By
import common_functions as additional
import time


def select_so(driver):
    if driver.title != "Sales Order":
        driver.find_element(By.ID, auth_data.so_main_button_id).click()
    assert "Sales Order", driver.title


def open_so_details(driver, url):
    additional.select_table_cell(driver, data.first_so_cell_id, "so", url)


def click_add_invoice(driver):
    driver.find_element(By.ID, data.generate_invoice_id).click()
    driver.find_element(By.XPATH, data.create_invoice).click()
    if driver.current_url == "https://crmtst.bai-inc.eu/index.php":
        driver.find_element(By.XPATH, data.create_new_btn).click()
    #   assert driver.current_url == 'http://crmtst_us.bai-inc.eu/index.php?module=Invoice&view=Edit'
    time.sleep(5)


def fill_in_invoice_no(driver):
    value = data.invoice_no_id
    text = str(additional.get_name())
    additional.fill_text_field(driver, value, text)


def fill_in_customer_po(driver):
    value = data.customer_po_id
    text = "Test Customer PO"
    additional.fill_text_field(driver, value, text)


def select_terms_of_sale(driver, url):
    time.sleep(3)
    value = data.terms_of_sale_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.tst_terms_of_sale
    else:
        text = data.qa_terms_of_sale
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_id
    text = data.terms_of_delivery
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_customer_no(driver):
    value = data.customer_no_id
    text = "Test customer No"
    additional.fill_text_field(driver, value, text)


def fill_in_sales_commision(driver):
    value = data.sales_commission_id
    text = "10"
    additional.fill_text_field(driver, value, text)


def fill_in_account(driver):
    value = data.account_id
    text = "Test account"
    additional.fill_text_field(driver, value, text)


def fill_in_boxes(driver):
    value = data.boxes_id
    text = "5"
    additional.fill_text_field(driver, value, text)


def fill_in_dimensions(driver):
    value = data.dimensions_id
    text = "Test demensions"
    additional.fill_text_field(driver, value, text)


def select_territory(driver):
    value = data.territory_id
    text = data.territory
    additional.select_value_from_dropdown(driver, value, text)


def select_due_date(driver):
    value = data.due_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def select_status(driver, url):
    value = data.status_id
    if url == "http://crmtst_us.bai-inc.eu/":
        text = data.tst_status
    else:
        text = data.qa_status
    additional.select_value_from_dropdown(driver, value, text)


def select_priority(driver):
    value = data.priority_id
    text = data.priority
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_place_of_delivery(driver):
    value = data.place_of_delivery_id
    text = "Test place of delivery"
    additional.fill_text_field(driver, value, text)


def select_ship_via(driver):
    value = data.ship_via_id
    text = data.ship_via
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_awb(driver):
    value = data.awb_id
    text = "Test awb"
    additional.fill_text_field(driver, value, text)


def fill_in_weight(driver):
    value = data.weight_id
    text = "5 pound(s)"
    additional.fill_text_field(driver, value, text)


def select_invoice_date(driver):
    value = data.invoice_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def select_order_date(driver):
    value = data.order_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def fill_in_total_payments(driver):
    value = data.total_payment_id
    text = "100"
    additional.fill_text_field(driver, value, text)


def fill_in_percent_paid(driver):
    value = data.percent_paid_id
    text = "5"
    additional.fill_text_field(driver, value, text)


def fill_in_billing_address(driver):
    field = data.billing_address_id
    text = "Test billing address"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_address(driver):
    field = data.shipping_address_id
    text = "Test Shipping Address"
    additional.fill_text_field(driver, field, text)

def fill_in_billing_address(driver):
    field = data.billing_address_id
    text = "Test billing address"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_address(driver):
    field = data.shipping_address_id
    text = "Test Shipping Address"
    additional.fill_text_field(driver, field, text)


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



def fill_in_special_note(driver):
    value = data.special_notes_id
    text = "Test special notes"
    additional.fill_text_field(driver, value, text)


def click_save_button(driver):
    driver.find_element(By.ID, "save_but").click()
    # assert driver.current_url.split('=3')[0] == data.after_creation_url


def check_values(driver):

    #   Text fields
    assert driver.find_element(By.ID, data.billing_address).text == values.billing_address
    assert driver.find_element(By.ID, data.billing_po_box).text == values.billing_po_box
    assert driver.find_element(By.ID, data.billing_city).text == values.billing_city
    assert driver.find_element(By.ID, data.billing_state).text == values.billing_state
    assert driver.find_element(By.ID, data.billing_post_code).text == values.billing_post_code
    assert driver.find_element(By.ID, data.billing_country).text == values.billing_country

    assert driver.find_element(By.ID, data.shipping_address).text == values.shipping_address
    assert driver.find_element(By.ID, data.shipping_po_box).text == values.shipping_po_box
    assert driver.find_element(By.ID, data.shipping_city).text == values.shipping_city
    assert driver.find_element(By.ID, data.shipping_state).text == values.shipping_state
    assert driver.find_element(By.ID, data.shipping_post_code).text == values.shipping_post_code
    assert driver.find_element(By.ID, data.shipping_country).text == values.shipping_country

from selenium.webdriver.common.by import By
from crm.data import quotes_data as data, authorization_data as auth_data, values_data as values
import common_functions as additional
import re, time


def select_quote(driver):
    if driver.title != "Quotes":
        driver.find_element(By.ID, auth_data.quotes_main_button_id).click()
    assert "Quotes", driver.title


def click_add_quote(driver, url):
    driver.find_element(By.ID, data.add_quote_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Quotes", driver.title)


def click_edit_quote(driver, url):
    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.ID, data.edit_quote_button_id).click()
    # assert (url + data.expected_url) == driver.current_url and ("Quotes", driver.title)
    new_url = None
    while new_url != 'http://crmqa.bai-inc.eu/index.php?module=Quotes&view=Edit&record=':
        index = re.search("\d", driver.current_url).start()
        new_url = driver.current_url[0:index]
        time.sleep(0.2)
    assert new_url == "http://crmqa.bai-inc.eu/index.php?module=Quotes&view=Edit&record="


def fill_in_account_field(driver):
    element_id = data.account_selector_id
    additional.wait_element(driver, data.account_selector_id, 'id')
    additional.select_first_cell(driver, element_id, True)


def fill_in_cust_ref(driver):
    field = data.cust_ref_id
    text = "Autotest Cust ref: 1245"
    additional.fill_text_field(driver, field, text)
    global gcustref
    gcustref = text


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


def select_quote_status(driver, url):
    value = data.quote_stage_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.tst_quote_stage
    else:
        text = data.qa_quote_stage
    additional.select_value_from_dropdown(driver, value, text)

    global gquotestage
    gquotestage = driver.find_element(By.ID, data.quote_stage_id).text


def fill_in_delivery(driver):
    field = data.delivery_id
    text = "Test delivery"
    additional.fill_text_field(driver, field, text)


def select_proirity(driver):
    value = data.priority_id
    text = data.priority
    additional.select_value_from_dropdown(driver, value, text)

    global gpriority
    gpriority = driver.find_element(By.ID, data.priority_id).text


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_id
    text = data.terms_of_delivery
    additional.select_value_from_dropdown(driver, value, text)

    global gtermsofdelivery
    gtermsofdelivery = driver.find_element(By.ID, data.terms_of_delivery_id).text


def select_terms_sale(driver, url):
    value = data.terms_of_sale_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.tst_terms_of_sale
    else:
        text = data.qa_terms_of_sale
    additional.select_value_from_dropdown(driver, value, text)

    global gtermsofsale
    gtermsofsale = driver.find_element(By.ID, data.terms_of_sale_id).text


def add_product(driver):
    value = data.product_list_button
    additional.select_first_cell(driver, value, False)


def select_location(driver):
    value = data.location_selector_id
    additional.select_first_cell(driver, value, False)

    # global gtermsofsale
    # gtermsofsale = driver.find_element(By.ID, data.location_id).text


def select_aircraft(driver):
    value = data.aircraft_selector_id
    additional.select_first_cell(driver, value, False)

    # global gaircraft
    # gaircraft = driver.find_element(By.ID, data.terms_of_sale_id).text


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

    # assert driver.find_element(By.ID, data.client_po).text == gcustref

    #   Quote number /n
    #   Condition
    #   Place of delivery
    #   Delivery
    #   Job
    #   QB No
    #   Terms & Conditions
    #   Description Details

    #   Dropdown

    assert driver.find_element(By.ID, data.terms_of_delivery_details_id).text == gtermsofdelivery
    assert driver.find_element(By.ID, data.terms_of_sale_details_id).text == gtermsofsale
    assert driver.find_element(By.ID, data.priority_details_id).text == gpriority
    assert driver.find_element(By.ID, data.quote_stage_details_id).text == gquotestage

    #   Assigned To
    #   Territory
    #   QB company
    #   QB Class

    #   Select from fields

    assert driver.find_element(By.ID, data.account).text == additional.gaccount
    assert driver.find_element(By.ID, data.location).text == additional.glocation
    assert driver.find_element(By.ID, data.aircraft).text == additional.gfleet
    # assert driver.find_element(By.ID, data.quoted_by).text + " " == additional.guser

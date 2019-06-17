from crm.data import so_data as data, authorization_data as auth_data, values_data as values
from selenium.webdriver.common.by import By
import common_functions as additional
import datetime
import time
import re


def click_edit_so(driver, url):

    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.ID, data.edit_so_button_id).click()
    # assert (url + data.expected_url) == driver.current_url and ("Quotes", driver.title)
    new_url = None
    if url == "https://crmtst.bai-inc.eu/":
        while new_url != 'https://crmtst.bai-inc.eu/index.php?module=SalesOrder&view=Edit&record=':
            index = re.search("\d", driver.current_url).start()
            new_url = driver.current_url[0:index]
            time.sleep(0.2)
        assert new_url == "https://crmtst.bai-inc.eu/index.php?module=SalesOrder&view=Edit&record="
    else:
        while new_url != 'https://crmqa.bai-inc.eu/index.php?module=SalesOrder&view=Edit&record=':
            index = re.search("\d", driver.current_url).start()
            new_url = driver.current_url[0:index]
            time.sleep(0.2)
        assert new_url == "https://crmqa.bai-inc.eu/index.php?module=SalesOrder&view=Edit&record="


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
    # additional.not_overwrite_selection(driver)


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
    global gclientpo
    gclientpo = text


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

    global gstatus
    gstatus = driver.find_element(By.ID, data.status_selector_id).text


def select_terms_of_payment(driver):
    value = data.terms_of_payment_id
    text = data.terms_of_payment_value
    additional.select_value_from_dropdown(driver, value, text)


def select_priority(driver):
    value = data.priority_id
    text = data.priority_value
    additional.select_value_from_dropdown(driver, value, text)

    global gpriority
    gpriority = driver.find_element(By.ID, data.priority_id).text


def select_terms_of_sale(driver):
    value = data.terms_of_sale_id
    text = data.terms_of_sale_value
    additional.select_value_from_dropdown(driver, value, text)

    global gtermsofsale
    gtermsofsale = driver.find_element(By.ID, data.terms_of_sale_id).text


def select_source(driver):
    value = data.source_id
    text = data.source_value
    additional.select_value_from_dropdown(driver, value, text)

    global gsource
    gsource = driver.find_element(By.ID, data.source_id).text


def select_ship_via(driver):
    value = data.ship_via_selector_id
    text = data.ship_via_value
    additional.select_value_from_dropdown(driver, value, text)

    global gshipvia
    gshipvia = driver.find_element(By.ID, data.ship_via_selector_id).text


def select_assigned_to(driver):
    value = data.assigned_to_selector_id
    text = data.assigned_to_value
    additional.select_value_from_dropdown(driver, value, text)

    global gassigned
    gassigned = driver.find_element(By.ID, data.assigned_to_selector_id).text


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_selector_id
    text = data.terms_of_delivery_value
    additional.select_value_from_dropdown(driver, value, text)

    global gdeliveryterms
    gdeliveryterms = driver.find_element(By.ID, data.terms_of_delivery_selector_id).text


def select_territory(driver, territory):
    value = data.territory_selector_id

    if territory == "ees":
        text = data.territory_ees_value
    elif territory == "bann-i":
        text = data.territory_bann_i_value
    elif territory == "bann-d":
        text = data.territory_bann_d_value

    additional.select_value_from_dropdown(driver, value, text)

    global gterritory
    gterritory = driver.find_element(By.ID, data.territory_selector_id).text


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


def select_due_date(driver):
    value = data.due_date_id
    date = '01-04-2019'
    additional.select_calendar_date(driver, value, date)


def add_product(driver):
    time.sleep(5)
    value = data.product_list_button
    additional.wait_element(driver, data.part_number_field_id, 'id')  #  additional.wait_element(driver, value, 'id')
    additional.select_first_cell(driver, value, False)


def save_so(driver):
    time.sleep(2)
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


def fill_in_billing_attention(driver):
    field = data.billing_attention_edit_id
    text = "Test Billing Attention"
    additional.fill_text_field(driver, field, text)


def fill_in_shipping_attention(driver):
    field = data.shipping_attention_edit_id
    text = "Test Shipping Attention"
    additional.fill_text_field(driver, field, text)


def fill_in_so_notes(driver):
    field = data.notes_id
    text = "Test Note"
    additional.fill_text_field(driver, field, text)


def check_stk_for_products(driver):
    product1 = data.from_stock_1_id
    product2 = data.from_stock_2_id
    driver.find_element(By.ID, product1).click()
    driver.find_element(By.ID, product2).click()


def check_values(driver):

    #   Text fields
    assert driver.find_element(By.ID, data.billing_address).text == values.billing_address
    assert driver.find_element(By.ID, data.billing_po_box).text == values.billing_po_box
    assert driver.find_element(By.ID, data.billing_city).text == values.billing_city
    assert driver.find_element(By.ID, data.billing_state).text == values.billing_state
    assert driver.find_element(By.ID, data.billing_post_code).text == values.billing_post_code
    assert driver.find_element(By.ID, data.billing_country).text == values.billing_country
    assert driver.find_element(By.ID, data.billing_attention_details_id).text == values.billing_attention

    assert driver.find_element(By.ID, data.shipping_address).text == values.shipping_address
    assert driver.find_element(By.ID, data.shipping_po_box).text == values.shipping_po_box
    assert driver.find_element(By.ID, data.shipping_city).text == values.shipping_city
    assert driver.find_element(By.ID, data.shipping_state).text == values.shipping_state
    assert driver.find_element(By.ID, data.shipping_post_code).text == values.shipping_post_code
    assert driver.find_element(By.ID, data.shipping_country).text == values.shipping_country
    assert driver.find_element(By.ID, data.shipping_attention_details_id).text == values.shipping_attention

    # assert driver.find_element(By.ID, data.client_po).text == gclientpo
    #   job
    #   QB no
    #   QB Class
    #   Terms & Conditions
    #    Notes

    #   Selected from fields
    assert driver.find_element(By.ID, data.account).text == additional.gaccount
    assert driver.find_element(By.ID, data.location).text == additional.glocation
    assert driver.find_element(By.ID, data.aircraft).text == additional.gfleet
    assert " " + driver.find_element(By.ID, data.sold_by).text == additional.guser
    assert driver.find_element(By.ID, data.assets).text == additional.gasset
    #   contract
    #   customer quote

    #   Dropdown fields
    assert driver.find_element(By.ID, data.status).text == gstatus
    assert driver.find_element(By.ID, data.assigned_to).text == gassigned
    assert driver.find_element(By.ID, data.terms_of_delivery).text == gdeliveryterms
    assert driver.find_element(By.ID, data.territory).text == gterritory
    assert driver.find_element(By.ID, data.ship_via).text == gshipvia
    assert driver.find_element(By.ID, data.priority).text == gpriority
    # assert driver.find_element(By.ID, data.terms_of_sale).text == gtermsofsale
    assert driver.find_element(By.ID, data.source_details).text == gsource

    #   QB Company


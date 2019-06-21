from crm.data import po_data as data, authorization_data as auth_data, values_data as values
from selenium.webdriver.common.by import By
import common_functions as additional
import time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def click_edit_po(driver, url):
    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.ID, data.edit_po_details_id).click()
    # assert (url + data.expected_url) == driver.current_url and ("Quotes", driver.title)
    new_url = None
    if url == "https://crmtst.bai-inc.eu/":
        while new_url != 'https://crmtst.bai-inc.eu/index.php?module=PurchaseOrder&view=Edit&record=':
            index = re.search("\d", driver.current_url).start()
            new_url = driver.current_url[0:index]
            time.sleep(0.2)
        assert new_url == "https://crmtst.bai-inc.eu/index.php?module=PurchaseOrder&view=Edit&record="
    else:
        while new_url != 'https://crmqa.bai-inc.eu/index.php?module=PurchaseOrder&view=Edit&record=':
            index = re.search("\d", driver.current_url).start()
            new_url = driver.current_url[0:index]
            time.sleep(0.2)
        assert new_url == "https://crmqa.bai-inc.eu/index.php?module=PurchaseOrder&view=Edit&record="


def select_po(driver):
    if driver.title != "Purchase Order":
        driver.find_element(By.ID, auth_data.po_main_button_id).click()
    assert "Sales Order", driver.title


def click_add_po(driver, url):
    driver.find_element(By.ID, data.add_po_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Purchase Orders", driver.title)


def select_vendor(driver):
    element_id = data.po_vendor_list_id
    additional.select_first_cell(driver, element_id, False)


def copy_vendor_address(driver):
    value = data.copy_vendor_address
    # while bool(additional.click_element_by_xpath(driver, value)) == True:
    #     try:
    driver.find_element(By.ID, data.vendor_po_box_id).send_keys(Keys.PAGE_DOWN)
    additional.click_element_by_xpath(driver, value)

    # except:
        #     elem = driver.find_element(By.XPATH, value)
        #     elem.send_keys(Keys.PAGE_DOWN)
    # value = data.vendor_po
    # text = "Test Vendor"
    # additional.fill_text_field(driver, value, text)


def copy_company_address(driver):
    additional.click_element_by_xpath(driver, data.copy_company_address)
    # value = data.vendor_po_box_id
    # text = "Test Vendor"
    # additional.fill_text_field(driver, value, text)


def add_product(driver):
    element_id = data.product_list_button
    additional.select_first_cell(driver, element_id, False)
    time.sleep(2)
    additional.wait_product_field_selection(driver)


def fill_in_vendor_po(driver):
    value = data.vendor_po_id
    text = "Test Vendor"
    additional.fill_text_field(driver, value, text)


def fill_in_tracking_number(driver):
    value = data.tracking_number_id
    text = "Test number"
    additional.fill_text_field(driver, value, text)


def select_due_date(driver):
    value = data.due_date_id
    date = '01-04-2018'
    additional.select_calendar_date(driver, value, date)


def fill_in_account(driver):
    field = data.account_id
    value = "Test account"
    additional.fill_text_field(driver, field, value)


def fill_in_delivery_place(driver):
    value = data.place_of_delivery_id
    text = "Test delivery place"
    additional.fill_text_field(driver, value, text)


def select_vendor(driver):
    element_id = data.po_vendor_list_id
    additional.select_first_cell(driver, element_id, False)


def fill_in_po_number(driver):
    value = data.po_number_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_in_requisition_number(driver):
    value = data.requisition_number_id
    text = "Test Requisition Number"
    additional.fill_text_field(driver, value, text)


def select_ship_via(driver):
    value = data.ship_via_id
    text = data.ship_via
    additional.select_value_from_dropdown(driver, value, text)


def select_status(driver):
    value = data.status_id
    text = data.status
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_sales_commission(driver):
    value = data.sales_commission_id
    text = "10"
    additional.fill_text_field(driver, value, text)


def fill_in_excise_duty(driver):
    value = data.excise_duty_id
    text = "11"
    additional.fill_text_field(driver, value, text)


def select_priority(driver):
    value = data.priority_id
    text = data.priority
    additional.select_value_from_dropdown(driver, value, text)


def select_status(driver):
    value = data.status_id
    text = data.status
    additional.select_value_from_dropdown(driver, value, text)


def select_risk(driver):
    value = data.po_risk_id
    text = data.low_risk_value
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_payment(driver, url):
    value = data.terms_of_payment_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.tst_terms_of_payment
    else:
        text = data.qa_terms_of_payment
    additional.select_value_from_dropdown(driver, value, text)


def select_assigned_to(driver):
    value = data.assigned_to_id
    text = data.assigned_to
    additional.select_value_from_dropdown(driver, value, text)


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_id
    text = data.terms_of_delivery
    additional.select_value_from_dropdown(driver, value, text)

#
# def select_territory(driver):
#     value = data.territory_id
#     text = data.territory
#     additional.select_value_from_dropdown(driver, value, text)


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
    gterritory = driver.find_element(By.ID, data.territory_id).text


def fill_in_vendor_po_box(driver):
    value = data.vendor_po_box_id
    text = "Test Vendor"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_city(driver):
    value = data.vendor_city_id
    text = "Test City"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_state(driver):
    value = data.vendor_state_id
    text = "Test State"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_post_code(driver):
    value = data.vendor_post_code_id
    text = "Test Postal Code"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_country(driver):
    value = data.vendor_country_id
    text = "Test Country"
    additional.fill_text_field(driver, value, text)


def fill_in_billing_attention(driver):
    value = data.billing_attention_id
    text = "Shipping Attention"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_po_box(driver):
    value = data.shipping_po_box_id
    text = "Test Vendor"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_city(driver):
    value = data.shipping_city_id
    text = "Test City"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_state(driver):
    value = data.shipping_state_id
    text = "Test State"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_post_code(driver):
    value = data.shipping_postal_code_id
    text = "Test Postal Code"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_country(driver):
    value = data.shipping_country_id
    text = "Test Country"
    additional.fill_text_field(driver, value, text)


def fill_in_shipping_attention(driver):
    value = data.shipping_attention_id
    text = "Shipping Attention"
    additional.fill_text_field(driver, value, text)


def select_aircraft(driver):
    element_id = data.aircraft_id
    additional.select_first_cell(driver, element_id, False)


def select_location(driver):
    element_id = data.location_id
    additional.select_first_cell(driver, element_id, False)


def select_contact_name(driver):
    element_id = data.contact_name_id
    additional.select_first_cell(driver, element_id, False)


def fill_in_description(driver):
    value = data.description_details_field
    text = "Test PO Description"
    additional.fill_text_field(driver, value, text)


def save_po(driver):
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)
    driver.find_element(By.ID, data.save_button_id).click()

# def fill_in_billing_address(driver):
#     billingid = data.billing_address_id
#     text = "Test billing address"
#     additional.fill_text_field(driver, billingid, text)


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


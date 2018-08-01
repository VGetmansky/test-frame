from crm.data import invoice_data as data, authorization_data as auth_data
from selenium.webdriver.common.by import By
import common_functions as additional


def open_so_details(driver, url):
    additional.select_table_cell(driver, data.first_so_cell_id, "so", url)


def click_add_invoice(driver):
    driver.find_element(By.ID, data.generate_invoice_id).click()
    driver.find_element(By.XPATH, data.create_invoice).click()
    if driver.current_url == "http://crmtst_us.bai-inc.eu/index.php":
        #value = data.overwrite_chk
        #button = data.create_new_btn
        #additional.overwrite_elements(driver, value, button)
        driver.find_element(By.XPATH, data.create_new_btn).click()
    #assert driver.current_url == 'http://crmtst_us.bai-inc.eu/index.php?module=Invoice&view=Edit'


def fill_in_invoice_no(driver):
    value = data.invoice_no_id
    text = str(additional.get_name())
    additional.fill_text_field(driver, value, text)


def fill_in_customer_po(driver):
    value = data.customer_po_id
    text = "Test Customer PO"
    additional.fill_text_field(driver, value, text)


def select_terms_of_sale(driver, url):
    value = data.terms_of_sale_id
    if url == "http://crmtst_us.bai-inc.eu/":
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


def fill_in_special_note(driver):
    value = data.special_notes_id
    text = "Test special notes"
    additional.fill_text_field(driver, value, text)


def click_save_button(driver):
    driver.find_element(By.ID, "save_but").click()
    # assert driver.current_url.split('=3')[0] == data.after_creation_url

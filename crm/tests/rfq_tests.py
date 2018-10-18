from crm.data import authorization_data as auth_data, rfq_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def select_rfq(driver):
    new_url = driver.current_url
    time.sleep(40)
    if driver.title != "Rfq":
        additional.wait_element_for_click(driver, auth_data.rfq_main_button_id)
        additional.wait_new_page(driver,  new_url)
    assert "Rfq", driver.title


def click_add_rfq(driver, url):
    new_url = driver.current_url
    additional.wait_element(driver, data.add_rfq_id, 'id')
    driver.find_element(By.ID, data.add_rfq_id).click()
    additional.wait_new_page(driver, new_url)

    time.sleep(10)
    additional.wait_element(driver, data.rfq_number_id, 'id')

    assert (url + data.expected_url) == driver.current_url and ("Rfq", driver.title)[0]


def fill_in_vendor_field(driver):
    element_id = data.vendor_list_id
    additional.wait_element(driver, element_id, 'id')
    additional.select_first_cell(driver, element_id, False)


def filter_by_creator(driver):
    # createdbyId = data.created_by_id
    # text = "Vladislav Getmansky"
    # additional.fill_text_field(driver, createdbyId, text)
    driver.find_element(By.XPATH, data.search_button).click()


def fill_in_account_field(driver):
    element_id = data.rfq_account_id
    time.sleep(3)
    #additional.wait_element(driver, element_id, 'id')
    additional.select_first_cell(driver, element_id, False)
    try:
        driver.find_element(By.XPATH, data.contact).click()
    except:
        return


def fill_in_contact_field(driver):
    element_id = data.rfq_contact_id
    additional.select_first_cell(driver, element_id, False)


def fill_in_customer_quote(driver):
    value = data.customer_quote_id
    text = "Test Customer Quote"
    additional.fill_text_field(driver, value, text)


def fill_in_received_via(driver):
    value = data.received_via_id
    text = "10"
    additional.fill_text_field(driver, value, text)


def select_sale_terms(driver, url):
    value = data.sale_terms_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.tst_sale_terms
    else:
        text = data.qa_sale_terms
    additional.select_value_from_dropdown(driver, value, text)


def select_delivery_terms(driver):
    value = data.delivery_terms_id
    text = data.delivery_terms
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_delivery_terms_text_field(driver):
    value = data.delivery_terms_field_id
    text = "Test Delivery terms"
    additional.fill_text_field(driver, value, text)


def fill_in_description(driver):
    value = data.description_id
    text = "Test Description"
    additional.fill_text_field(driver, value, text)


def select_territory(driver):
    value = data.territory_id
    text = data.territory
    additional.select_value_from_dropdown(driver, value, text)


def select_pl_status(driver):
    value = data.pl_status_id
    text = data.pl_status
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_aircraft_field(driver):
    element_id = data.rfq_aircraft_id
    additional.select_first_cell(driver, element_id, False)


def fill_in_location_field(driver):
    element_id = data.rfq_location_id
    additional.select_first_cell(driver, element_id, False)


def select_priority(driver):
    value = data.priority_id
    text = data.priority
    additional.select_value_from_dropdown(driver, value, text)


def fill_note(driver):
    value = data.notes_id
    text = "Note"
    additional.fill_text_field(driver, value, text)


def fill_non_printed_note(driver):
    value = data.non_printed_notes_id
    text = "Note"
    additional.fill_text_field(driver, value, text)


def fill_v_quote(driver):
    value = data.v_quote_id
    text = "V.Quote"
    additional.fill_text_field(driver, value, text)


# stock outright
def fill_in_unit_cost(driver):
    value = data.unit_cost_id
    text = "12"
    additional.fill_text_field(driver, value, text)


def fill_in_unit_price(driver):
    value = data.stock_out_unit_price_id
    text = "15"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_moq(driver):
    value = data.vendor_moq_id
    text = "2"
    additional.fill_text_field(driver, value, text)


def fill_in_moq(driver):
    value = data.moq_id
    text = "15"
    additional.fill_text_field(driver, value, text)


def fill_in_qty(driver):
    value = data.stock_out_qty_id
    text = "20"
    additional.fill_text_field(driver, value, text)


def fill_in_lead_time(driver):
    value = data.stock_out_lead_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)


def fill_in_delivery_time(driver):
    value = data.stock_out_delivery_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)


def fill_in_min_vendor_order(driver):
    value = data.stock_out_min_vendor_order_id
    text = "1"
    additional.fill_text_field(driver, value, text)


def click_offer(driver):
    value = data.offer_id
    additional.wait_element_for_click(driver, value)
    driver.find_element(By.XPATH, '//label[@class="checkbox-label" and @for="line_check_1"]').click()


def click_alt_offer(driver):
    value = data.save_and_alt_offer_id
    type = "id"
    additional.wait_element(driver, value, type).click()
    additional.wait_element(driver, '//a[contains(., "Create New line")]', 'xpath')
    additional.click_element_by_xpath(driver, '//a[contains(., "Create New line")]')


def click_add_part_number(driver):
    driver.find_element(By.ID, data.add_part_line_id).click()
    # assert (url + data.expected_url) == driver.current_url and ("Rfq", driver.title)


def fill_part_number_name(driver):
    value = data.partnumber_id
    text = "PSE-301"
    additional.fill_pn_fields(driver, value, text)


def fill_pn_qty(driver):
    value = data.partnumber_qty_id
    text = "10"
    additional.fill_pn_fields(driver, value, text)


def fill_in_stock_outright_lead_time(driver):
    value = data.stock_out_lead_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)


def fill_in_stock_outright_delivery_time(driver):
    value = data.stock_out_delivery_time_id
    text = '14'
    additional.fill_text_field(driver, value, text)


def click_insert_pn(driver):
    value = data.insert_part_number_id
    text = None
    additional.fill_pn_fields(driver, value, text)
    additional.wait_element_vanishing(driver, value)
    time.sleep(3)

# def click_search_vendor_button(driver):
#     value = data.vendor_search_id
#     driver.find_element(By.ID, value).click()


def fill_in_vendor(driver):
    element_id = data.rfq_vendor_id
    # time.sleep(5)
    additional.select_first_cell(driver, element_id, False)
    try:
        driver.find_element(By.XPATH, data.contact).click()
    except:
        return


def fill_in_pn_description(driver):
    field = data.pn_description_id
    text = "Test description"
    additional.fill_text_field(driver, field, text)


def fill_in_plli_aval_qty(driver):
    field = data.spli_aval_qty_id
    text = "10"
    additional.fill_text_field(driver, field, text)


# exchange
def select_exchange_type(driver):
    value = data.spli_sales_type_id
    text = 'Exchange'
    time.sleep(3)
    additional.change_sales_type(driver, value, text)
    additional.wait_element(driver, data.ex_fee_cost_id, 'id')


def select_repair_type(driver):
    value = data.spli_sales_type_id
    text = 'Repair/OH'
    time.sleep(3)
    additional.change_sales_type(driver, value, text)
    additional.wait_element(driver, data.repair_b_check_price_id, 'id')


def fill_in_exchange_fee_cost(driver):
    value = data.ex_fee_cost_id
    text = '13'
    additional.wait_element(driver, data.ex_fee_cost_id, 'id')
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_vendor_rtrn_days(driver):
    value = data.ex_vendor_rtnr_days_id
    text = '3'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_service_cost(driver):
    value = data.ex_service_cost_id
    text = '5'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_ber_cost(driver):
    value = data.ex_ber_cost_id
    text = '7'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_lead_time(driver):
    value = data.ex_lead_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_cost_total(driver):
    value = data.ex_lead_time_id
    text = '9'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_qty(driver):
    value = data.ex_qty_id
    text = '5'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_fee_price(driver):
    value = data.ex_fee_price_id
    text = '12'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_cust_rtrn_days(driver):
    value = data.ex_cust_rtnr_days_id
    text = '8'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_service_price(driver):
    value = data.ex_service_price_id
    text = '15'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_ber_price(driver):
    value = data.ex_ber_price_id
    text = '3'
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_delivery_time(driver):
    value = data.ex_delivery_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)


# repair
def fill_in_repair_bcheck_cost(driver):
    value = data.b_check_cost_id
    text = '25'
    additional.wait_element_for_click(driver, data.b_check_cost_id)
    additional.fill_text_field(driver, value, text)


def fill_in_repair_lead_b_check(driver):
    value = data.lead_b_check_id
    text = '14'
    additional.fill_text_field(driver, value, text)


def fill_in_avg_repair_cost(driver):
    value = data.avg_repair_cost_id
    text = '25'
    additional.fill_text_field(driver, value, text)


def fill_in_max_repair_cost(driver):
    value = data.max_repair_cost_id
    text = '30'
    additional.fill_text_field(driver, value, text)


def fill_in_repair_lead_time(driver):
    value = data.repair_lead_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)


def fill_in_repair_qty(driver):
    value = data.repair_qty_id
    text = '10'
    additional.fill_text_field(driver, value, text)


def fill_in_repair_bcheck_price(driver):
    value = data.repair_b_check_price_id
    text = '12'
    additional.fill_text_field(driver, value, text)


def fill_in_repair_delivery_b_check(driver):
    value = data.repair_delivery_b_check_id
    text = '12'
    additional.fill_text_field(driver, value, text)


def fill_in_avg_repair_price(driver):
    value = data.avg_repair_price_id
    text = '7'
    additional.fill_text_field(driver, value, text)


def fill_in_max_repair_price(driver):
    value = data.max_repair_price_id
    text = '25'
    additional.fill_text_field(driver, value, text)


def fill_in_repair_delivery_time(driver):
    value = data.repair_delivery_time_id
    text = '14'
    additional.fill_text_field(driver, value, text)


def click_save_rfq(driver):
    driver.execute_script("window.scrollTo(0, 0)")
    additional.click_element_by_id(driver, data.save_rfq_id)
    additional.wait_element(driver, data.rfq_create_quote_id, 'id')

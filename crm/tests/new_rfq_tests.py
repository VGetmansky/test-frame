from crm.data import authorization_data as auth_data, new_rfq_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time, re

from selenium.webdriver.common.keys import Keys


def select_rfq(driver):
    new_url = driver.current_url
    time.sleep(3)
    if driver.title != "Rfq":
        additional.wait_element_for_click(driver, auth_data.rfq_main_button_id)
        additional.wait_new_page(driver, new_url)
    assert "Rfq", driver.title and driver.current_url == "http://crmqa.bai-inc.eu/index.php?module=Rfq&view=List"


def click_add_rfq(driver, url):

    new_url = driver.current_url
    additional.wait_element(driver, data.add_rfq_id, 'id')
    driver.find_element(By.ID, data.add_rfq_id).click()
    additional.wait_new_page(driver, new_url)

    time.sleep(5)
    # additional.wait_element(driver, data.rfq_number_id, 'id')
    assert data.new_qa_rfq_url == driver.current_url or data.new_tst_rfq_url == driver.current_url and (data.new_rfq_title, driver.title)[0]


def fill_in_vendor_field(driver):
    element_id = data.rfq_vendor_search_id
    time.sleep(3)

    additional.wait_element(driver, element_id, 'id')
    driver.find_element(By.ID, element_id).click()

    elem = driver.find_element(By.ID, data.rfq_search_value_id)
    text = "Autotest User"
    additional.wait_element(driver, data.rfq_search_value_id, 'id')
    #time.sleep(3)
    driver.find_element(By.ID, data.rfq_search_value_id).click()
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)

    time.sleep(3)

    text = data.rfq_vendor_first_field
    additional.wait_element(driver, text, 'xpath')
    length = len(driver.find_elements(By.XPATH, text))
    driver.find_elements(By.XPATH, text)[length - 1].click()


def filter_by_creator(driver):
    # createdbyId = data.created_by_id
    # text = "Vladislav Getmansky"
    # additional.fill_text_field(driver, createdbyId, text)
    driver.find_element(By.XPATH, data.search_button).click()


def fill_in_account_field(driver):
    element_id = data.rfq_search_account_id
    time.sleep(15)

    additional.wait_element(driver, element_id, 'id')
    driver.find_element(By.ID, element_id).click()

    elem = driver.find_element(By.ID, data.rfq_search_value_id)
    text = "Autotest"
    time.sleep(15)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, data.rfq_search_value_id)))

    additional.wait_element(driver, data.rfq_search_value_id, 'id')
    time.sleep(15)
    driver.find_element(By.ID, data.rfq_search_value_id).click()
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)

    time.sleep(3)
    additional.wait_element(driver, data.rfq_account_first_field, 'xpath')
    driver.find_element(By.XPATH, data.rfq_account_first_field).click()


def fill_in_contact_field(driver):

    element_id = data.rfq_search_contact_id
    time.sleep(3)

    additional.wait_element(driver, element_id, 'id')
    driver.find_element(By.ID, element_id).click()

    elem = driver.find_element(By.ID, data.rfq_search_value_id)
    text = "Autotest"
    additional.wait_element(driver, data.rfq_search_value_id, 'id')
    driver.find_element(By.ID, data.rfq_search_value_id).click()
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)

    time.sleep(3)
    additional.wait_element(driver, data.rfq_contact_first_field, 'xpath')
    driver.find_element(By.XPATH, data.rfq_contact_first_field).click()


def fill_in_pli_location(driver):
    value = data.rfq_pn_location_id
    text = "Test Location"
    additional.fill_text_field(driver, value, text)


def fill_in_customer_quote(driver):
    value = data.rfq_customer_quote_id
    text = "Test Customer Quote"
    additional.fill_text_field(driver, value, text)


def fill_in_received_via(driver):
    value = data.rfq_received_via_id
    text = "10"
    additional.fill_text_field(driver, value, text)


def select_sale_terms(driver, url):
    value = data.rfq_terms_of_sale_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.rfq_tst_sale_terms
    else:
        text = data.rfq_qa_sale_terms
    additional.select_value_from_dropdown(driver, value, text)


def select_delivery_terms(driver):
    value = data.rfq_terms_of_delivery_id
    text = data.rfq_delivery_terms
    additional.select_value_from_dropdown(driver, value, text)


def fill_in_delivery_terms_text_field(driver):
    value = data.delivery_terms_field_id
    text = "Test Delivery terms"
    additional.fill_text_field(driver, value, text)


def fill_in_description(driver):
    value = data.rfq_description_id
    text = "Test Description"
    additional.fill_text_field(driver, value, text)


def fill_in_place_of_delivery(driver):
    value = data.rfq_place_of_delivery_id
    text = "Test Place of Delivery"
    additional.fill_text_field(driver, value, text)


def select_territory(driver):
    value = data.rfq_territory_id
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
    value = data.rfq_priority_id
    text = data.rfq_routine_proirity
    additional.select_value_from_dropdown(driver, value, text)


def select_status(driver):
    value = data.rfq_status_id
    text = data.rfq_planning_status
    additional.select_value_from_dropdown(driver, value, text)


def select_assigned_to(driver):
    value = data.rfq_assigned_to_id
    text = data.rfq_assigned_to
    additional.select_value_from_dropdown(driver, value, text)


def fill_note(driver):
    value = data.rfq_notes_id
    text = "Test Note"
    additional.fill_text_field(driver, value, text)


def fill_non_printed_note(driver):
    value = data.rfq_non_printed_notes_id
    text = "Test non-printed Note"
    additional.fill_text_field(driver, value, text)


def fill_v_quote(driver):
    value = data.rfq_v_quote_id
    text = "V.Quote"
    additional.fill_text_field(driver, value, text)


# stock outright
def fill_in_unit_cost(driver):
    value = data.so_stock_unit_cost_id
    text = "12"
    additional.fill_text_field(driver, value, text)


def fill_in_unit_price(driver):
    value = data.so_unit_price_id
    text = "15"
    additional.fill_text_field(driver, value, text)


def fill_in_vendor_moq(driver):
    value = data.so_vendor_moq_id
    text = "2"
    additional.fill_text_field(driver, value, text)


def fill_in_moq(driver):
    value = data.so_stock_moq_id
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


def fill_in_tags(driver):
    value = data.rfq_pn_tags_id
    certtype = data.rfq_cert_type_id
    cert = data.rfq_pn_cert

    additional.wait_element(driver, value, 'id')
    driver.find_element(By.ID, value).click()

    additional.wait_element(driver, certtype, 'id')
    driver.find_element(By.ID, certtype).click()

    additional.wait_element(driver, cert, 'xpath')
    driver.find_element(By.XPATH, cert).click()

    assert driver.find_element(By.XPATH, '//span[contains(., "CofC Only")]')


def fill_in_condition(driver):

    condition = data.rfq_pn_condition_id
    conditionval = data.rfq_pn_condition

    conditionval = "//li[contains(., 'NE')]"
    # additional.wait_element(driver, condition, 'id')
    driver.find_element(By.ID, condition).click()

    additional.wait_element(driver, conditionval, 'xpath')
    length = len(driver.find_elements(By.XPATH, conditionval))
    driver.find_elements(By.XPATH, conditionval)[length - 1].click()


def save_and_offer(driver):
    value = data.rfq_pn_save_and_offer_id
    newline = data.rfq_create_new_line
    # additional.wait_element(driver, value, 'id')
    driver.find_element(By.ID, value).click()
    additional.wait_element(driver, newline, 'xpath')
    driver.find_element(By.XPATH, newline).click()

    accept_vrp_description(driver, "Current")


def click_offer(driver):
    value = data.offer_id
    additional.wait_element_for_click(driver, value)
    driver.find_element(By.XPATH, '//label[@class="checkbox-label" and @for="line_check_1"]').click()

    accept_vrp_description(driver, "Current")


def click_alt_offer(driver):
    value = data.rfq_pn_alt_offer_id
    type = "id"
    additional.wait_element(driver, value, type).click()

    accept_vrp_description(driver, "Current")


def accept_vrp_description(driver, description):

    time.sleep(2)
    if description == "Current":

        try:
            driver.find_element(By.ID, data.current_description_id)

            if driver.find_element(By.ID, data.current_description_id).is_displayed():
                driver.find_element(By.ID, data.current_description_id).click()
                driver.find_element(By.ID, data.vrq_accept_id).click()
            else:
                return

        except NoSuchElementException:
            return

    elif description == "Recommended":

        try:
            driver.find_element(By.ID, data.recommended_description_id)

            if driver.find_element(By.ID, data.recommended_description_id).is_displayed():
                driver.find_element(By.ID, data.recommended_description_id).click()
                driver.find_element(By.ID, data.vrq_accept_id).click()
            else:
                return

        except NoSuchElementException:
            return

    elif description == "Stored":

        try:
            driver.find_element(By.ID, data.stored_description_id)

            if driver.find_element(By.ID, data.stored_description_id).is_displayed():
                driver.find_element(By.ID, data.stored_description_id).click()
                driver.find_element(By.ID, data.vrq_accept_id).click()
            else:
                return

        except NoSuchElementException:
            return

    else:
        return


def click_add_part_number(driver):
    driver.find_element(By.ID, data.add_part_line_id).click()
    # assert (url + data.expected_url) == driver.current_url and ("Rfq", driver.title)


def fill_part_number_name(driver):
    value = data.rfq_add_part_id
    text = "DK120 ^ DESCRIPTION ^ 10"
    pn_text_field = data.rfq_part_add_multi_id
    addpn = data.rfq_add_to_list_button_id
    additional.fill_new_pn_fields(driver, value, pn_text_field, addpn, text)


def uncheck_will_advice(driver):
    value = data.rfq_will_advice_check_id
    driver.find_element(By.ID, value).click()


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
    field = data.rfq_pn_description_id
    text = "Test description"
    additional.fill_text_field(driver, field, text)


def fill_in_pli_aval_qty(driver):
    field = data.rfq_qty_avail_id
    text = "10"
    additional.fill_text_field(driver, field, text)


def fill_in_pli_location(driver):
    field = data.rfq_pn_location_id
    text = "Test Location"
    additional.fill_text_field(driver, field, text)


def fill_in_pli_rate(driver):
    field = data.rfq_pn_rate_id
    text = "0.25"
    additional.fill_text_field(driver, field, text)


# exchange
def select_exchange_type(driver):
    value = data.rfq_pn_salestype_id
    text = data.rfq_exchange
    time.sleep(1)

    # additional.wait_element(driver, value, 'id')
    driver.find_element(By.ID, value).click()

    additional.wait_element(driver, text, 'xpath')
    length = len(driver.find_elements(By.XPATH, text))
    driver.find_elements(By.XPATH, text)[length - 1].click()

    # additional.change_sales_type(driver, value, text)
    # additional.wait_element(driver, data.ex_fee_cost_id, 'id')


def select_repair_type(driver):
    value = data.rfq_pn_salestype_id
    text = 'Repair/OH'
    time.sleep(3)
    additional.change_sales_type(driver, value, text)
    # additional.wait_element(driver, data.repair_b_check_price_id, 'id')


def fill_in_exchange_fee_cost(driver):
    value = data.ex_fee_cost_id
    text = '13'
    additional.wait_element(driver, data.ex_fee_cost_id, 'id')
    additional.fill_text_field(driver, value, text)


def fill_in_exchange_vendor_rtrn_days(driver):
    value = data.ex_vendor_rtrn_days_id
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
    value = data.ex_cust_rtrn_price_id
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

def select_repair_type(driver):
    value = data.rfq_pn_salestype_id
    text = data.rfq_repair
    time.sleep(1)

    # additional.wait_element(driver, value, 'id')
    driver.find_element(By.ID, value).click()

    additional.wait_element(driver, text, 'xpath')
    length = len(driver.find_elements(By.XPATH, text))
    driver.find_elements(By.XPATH, text)[length - 1].click()


def fill_in_repair_bcheck_cost(driver):
    value = data.repair_b_check_cost_id
    text = '25'
    additional.wait_element_for_click(driver, value)
    additional.fill_text_field(driver, value, text)


def fill_in_repair_lead_b_check(driver):
    value = data.repair_lead_b_check_id
    text = '14'
    additional.fill_text_field(driver, value, text)


def fill_in_avg_repair_cost(driver):
    value = data.repair_avg_repair_cost_id
    text = '25'
    additional.fill_text_field(driver, value, text)


def fill_in_max_repair_cost(driver):
    value = data.repair_max_cost_id
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
    value = data.repair_avg_repair_price_id
    text = '7'
    additional.fill_text_field(driver, value, text)


def fill_in_max_repair_price(driver):
    value = data.repair_max_price_id
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


def save_and_quote(driver, url):
    value = data.rfq_save_button_id
    action = data.rfq_save_and_quote_id
    quote = data.creqte_new_quote_button

    time.sleep(3)

    driver.find_element(By.ID, value).click()
    driver.find_element(By.ID, action).click()
    additional.wait_element(driver, quote, 'xpath')
    time.sleep(5)

    #   url_before = driver.current_url

    driver.find_element(By.XPATH, quote).click()

    # index = re.search("\d", driver.current_url).start()
    # new_url = driver.current_url[0:index]
    # quotedetailsurl = 'http://crmqa.bai-inc.eu/index.php?module=Quotes&view=Detail&record='
    # additional.wait_new_page(driver, new_url)
    time.sleep(2)
    assert driver.current_url.split('=')[1] == "Quotes&view"

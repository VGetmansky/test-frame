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
    # time.sleep(15)

    additional.wait_element(driver, element_id, 'id')
    driver.find_element(By.ID, element_id).click()

    elem = driver.find_element(By.ID, data.rfq_search_value_id)
    text = "Autotest"
    # time.sleep(15)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, data.rfq_search_value_id)))

    additional.wait_element(driver, data.rfq_search_value_id, 'id')
    # time.sleep(15)
    driver.find_element(By.ID, data.rfq_search_value_id).click()
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)

    time.sleep(3)
    additional.wait_element(driver, data.rfq_account_first_field, 'xpath')
    driver.find_element(By.XPATH, data.rfq_account_first_field).click()
    assert additional.get_property_value(driver, data.rfq_account_id, "id") == 'Account for autotests', \
        "Wrong Account Name Value!"


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
    assert additional.get_property_value(driver, data.rfq_contact_id, "id") == 'Autotest User', "Wrong Contact Value!"


def fill_in_pli_location(driver):
    value = data.rfq_pn_location_id
    text = "Test Location"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Text Location Value!"


def fill_in_customer_quote(driver):
    value = data.rfq_customer_quote_id
    text = "Test Customer Quote"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Customer Quote Value!"


def fill_in_received_via(driver):
    value = data.rfq_received_via_id
    text = "10"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Received Via Value!"


def select_sale_terms(driver, url):
    value = data.rfq_terms_of_sale_id
    if url == "https://crmtst.bai-inc.eu/":
        text = data.rfq_tst_sale_terms
    else:
        text = data.rfq_qa_sale_terms
    additional.select_value_from_dropdown(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == 'NET-30', "Wrong Terms of Sale Value!"


def select_delivery_terms(driver):
    value = data.rfq_terms_of_delivery_id
    text = data.rfq_delivery_terms
    additional.select_value_from_dropdown(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == 'CIF', "Wrong Terms of Delivery Value!"


def fill_in_delivery_terms_text_field(driver):
    value = data.delivery_terms_field_id
    text = "Test Delivery terms"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Delivery Terms Value!"


def fill_in_description(driver):
    value = data.rfq_description_id
    text = "Test Description"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == "Test Description", "Wrong Test Description Value!"


def fill_in_place_of_delivery(driver):
    value = data.rfq_place_of_delivery_id
    text = "Test Place of Delivery"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == "Test Place of Delivery", \
        "Wrong Place of Delivery Value!"


def select_territory(driver):
    value = data.rfq_territory_id
    text = data.territory
    additional.select_value_from_dropdown(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == 'US', "Wrong Territory Value!"


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
    assert additional.get_property_value(driver, value, "id") == "Routine",  "Wrong Priority Value!"


def select_status(driver):
    value = data.rfq_status_id
    text = data.rfq_planning_status
    additional.select_value_from_dropdown(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == 'Planning',  "Wrong Status Value!"


def select_assigned_to(driver):
    value = data.rfq_assigned_to_id
    text = data.rfq_assigned_to
    additional.select_value_from_dropdown(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == 'Administrator',  "Wrong Assigned To Value!"


def fill_note(driver):
    value = data.rfq_notes_id
    text = "Test Note"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Note Value!"


def fill_non_printed_note(driver):
    value = data.rfq_non_printed_notes_id
    text = "Test non-printed Note"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text,  "Wrong non-printed Note Value!"


def fill_v_quote(driver):
    value = data.rfq_v_quote_id
    text = "V.Quote"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong V.Quote Value!"


# stock outright
def fill_in_unit_cost(driver):
    value = data.so_stock_unit_cost_id
    text = "12"
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Unit Cost Value"
    # unit price
    assert float(additional.get_property_value(driver, data.so_unit_price_id, "id")) == \
           float((float(additional.get_property_value(driver, value, "id"))) / float(
               additional.get_property_value(driver, data.rfq_pn_rate_id,
                                             "id"))), " Гnit price value recalculated incorrectly!!"
    # total cost
    assert float(additional.get_property_value(driver, data.so_stock_total_cost_id, "id")) == \
           float((float(additional.get_property_value(driver, value, "id"))) * float(
               additional.get_property_value(driver, data.so_stock_qty_id,
                                             "id"))), "Total cost Value recalculated incorrectly!!"
    # total price
    assert float(additional.get_property_value(driver, data.so_stock_total_price_id, "id")) == \
           float((float(additional.get_property_value(driver, data.so_unit_price_id, "id"))) * float(
               additional.get_property_value(driver, data.so_stock_qty_id,
                                             "id"))), "Total Price Value recalculated incorrectly!!"
    # MGM $
    assert float(additional.get_property_value(driver, data.so_mgm_id, "id")) == \
           round((float(((float(additional.get_property_value(driver, data.so_unit_price_id, "id"))) - (
               float(additional.get_property_value(driver, value, "id")))) * float(
               additional.get_property_value(driver, data.so_stock_qty_id, "id")))), 2), "Total MGM recalculated incorrectly!!"
    # MGM %
    total_price = float(additional.get_property_value(driver, data.so_unit_price_id, "id")) * float(additional.get_property_value(driver, data.so_stock_qty_id, "id"))
    qty = float(additional.get_property_value(driver, data.so_stock_qty_id, "id"))
    total_cost = float(additional.get_property_value(driver, data.so_stock_unit_cost_id, "id")) * float(additional.get_property_value(driver, data.so_stock_qty_id, "id"))

    assert float(additional.get_property_value(driver, data.so_mgm_percent_id, "id")) == \
           (total_price - total_cost)/total_cost * 100, "Total MGM recalculated incorrectly!!"


def fill_in_unit_price(driver):
    value = data.so_unit_price_id
    text = "15"
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Unit Price Value!"
    assert additional.get_property_value(driver, data.rfq_pn_rate_id, 'id') == "0.80", "Rate value recalculated incorrectly"


def fill_in_vendor_moq(driver):
    value = data.so_vendor_moq_id
    text = "2"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Vendor MOQ Value!"


def fill_in_moq(driver):
    value = data.so_stock_moq_id
    text = "15"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong V.Quote Value!"


def fill_in_qty(driver):
    value = data.stock_out_qty_id
    text = "20"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text,  "Wrong Delivery Stock Out Qty Value!"


def fill_in_lead_time(driver):
    value = data.stock_out_lead_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text,  "Wrong Stock Out Lead Time Value!"


def fill_in_delivery_time(driver):
    value = data.stock_out_delivery_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text,  "Wrong Delivery Time Value!"


def fill_in_min_vendor_order(driver):
    value = data.stock_out_min_vendor_order_id
    text = "1"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Min.Vendor Order Value!"


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

    assert driver.find_element(By.XPATH, '//span[contains(., "CofC Only")]'),  "Can't select Cert type Value!"


def fill_in_condition(driver):

    condition = data.rfq_pn_condition_id
    conditionval = data.rfq_pn_condition

    conditionval = "//li[contains(., 'NE')]"
    # additional.wait_element(driver, condition, 'id')
    driver.find_element(By.ID, condition).click()

    additional.wait_element(driver, conditionval, 'xpath')
    length = len(driver.find_elements(By.XPATH, conditionval))
    driver.find_elements(By.XPATH, conditionval)[length - 1].click()
    assert additional.get_property_value(driver, condition, "id") == "NE", "Wrong Min.Vendor Order Value!"


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
    assert additional.get_property_value(driver, value, "id") == text, "Wrong PN Qty Value!"


def fill_in_stock_outright_lead_time(driver):
    value = data.stock_out_lead_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Lead TIme Value!"


def fill_in_stock_outright_delivery_time(driver):
    value = data.stock_out_delivery_time_id
    text = '14'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Delivery Time Value!"


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
    assert additional.get_property_value(driver, field, "id") == text, "Wrong PN Description Value!"


def fill_in_pli_aval_qty(driver):
    field = data.rfq_qty_avail_id
    text = "10"
    additional.fill_text_field(driver, field, text)
    assert additional.get_property_value(driver, field, "id") == text, "Wrong Qty Aval Value!"


def fill_in_pli_location(driver):
    field = data.rfq_pn_location_id
    text = "Test Location"
    additional.fill_text_field(driver, field, text)
    assert additional.get_property_value(driver, field, "id") == text, "Wrong Location Value!"


def fill_in_pli_rate(driver):
    field = data.rfq_pn_rate_id
    text = "0.25"
    additional.fill_text_field(driver, field, text)
    assert additional.get_property_value(driver, field, "id") == text, "Wrong Rate Value!"


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
    assert additional.get_property_value(driver, value, "id") == "Exchange", "Wrong Sales Type Value!"


def select_repair_type(driver):
    value = data.rfq_pn_salestype_id
    text = 'Repair/OH'
    time.sleep(3)
    additional.change_sales_type(driver, value, text)
    # additional.wait_element(driver, data.repair_b_check_price_id, 'id')
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Sales Type Value!"


def fill_in_exchange_fee_cost(driver):
    value = data.ex_fee_cost_id
    text = '13'
    additional.wait_element(driver, data.ex_fee_cost_id, 'id')
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Exchange Fee Cost Value!"
    assert additional.get_property_value(driver, data.ex_fee_price_id, "id") == "16.2500", "Exchange Fee Price Value recalculated incorrectly!!"


def fill_in_exchange_vendor_rtrn_days(driver):
    value = data.ex_vendor_rtrn_days_id
    text = '3'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Vendor RTRN Days Value!"


def fill_in_exchange_service_cost(driver):
    value = data.ex_service_cost_id
    text = '5'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Service Cost Value!"


def fill_in_exchange_ber_cost(driver):
    value = data.ex_ber_cost_id
    text = '7'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Ber Cost Value!"
    assert int(additional.get_property_value(driver, value, "id")) == \
           int((float(additional.get_property_value(driver, data.ex_ber_price_id, "id"))) * float(
               additional.get_property_value(driver, data.rfq_pn_rate_id, "id"))), "Ber Price Value recalculated incorrectly!!"


def fill_in_exchange_lead_time(driver):
    value = data.ex_lead_time_id
    text = "7"
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Lead Time Value!"
    assert additional.get_property_value(driver, data.ex_delivery_time_id, "id") == text, "Delivery Time Value recalculated incorrectly!"


def fill_in_exchange_cost_total(driver):
    value = data.ex_lead_time_id
    text = '9'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Lead Time Value!"


def fill_in_exchange_qty(driver):
    value = data.ex_qty_id
    text = '5'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Exchange Qty Value!"
    assert additional.get_property_value(driver, data.ex_cost_total_id, "id") == "90.00", "Wrong Exchange Cost Value recalculated incorrectly!"
    assert additional.get_property_value(driver, data.ex_total_price_id, "id") == "112.50", "Wrong Exchange Total Value recalculated incorrectly!"
    assert additional.get_property_value(driver, data.ex_mgm_id, "id") == "22.50", "Wrong Exchange MGM Value recalculated incorrectly!"


def fill_in_exchange_fee_price(driver):
    value = data.ex_fee_price_id
    text = '12'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Fee Price Value!"
    assert additional.get_property_value(driver, data.ex_ber_price_id, "id") == "6.4815", "Ber Price Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.ex_service_price_id, "id") == "4.6296", "Ber Price Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.ex_total_price_id, "id") == "83.15", "Total Price Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.ex_mgm_id, "id") == "-6.85", "MGM Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.ex_mgm_percent_id, "id") == "-7.61", "MGM Price Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.rfq_pn_rate_id, "id") == "1.08", "Rate Value recalculated incorrectly!!"


def fill_in_exchange_cust_rtrn_days(driver):
    value = data.ex_cust_rtrn_price_id
    text = '8'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Cust RTRN Price Value!"


def fill_in_exchange_service_price(driver):
    value = data.ex_service_price_id
    text = '15'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Service Price Value!"
    assert additional.get_property_value(driver, data.ex_mgm_id, "id") == "45.00", "MGM Value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.ex_mgm_percent_id, "id") == "50.00", "MGM Price Value recalculated incorrectly!!"


def fill_in_exchange_ber_price(driver):
    value = data.ex_ber_price_id
    text = '3'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Ber Price Value!"


def fill_in_exchange_delivery_time(driver):
    value = data.ex_delivery_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Delivery Time Value!"


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
    assert additional.get_property_value(driver, value, "id") == "Repair/OH", "Wrong Type value!"


def fill_in_repair_bcheck_cost(driver):
    value = data.repair_b_check_cost_id
    text = '25'
    additional.wait_element_for_click(driver, value)
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair B-Check Value!"
    assert float(additional.get_property_value(driver, data.repair_b_check_price_id, "id")) == \
           round(float(additional.get_property_value(driver, value, "id")) / float(additional.get_property_value(driver, data.rfq_pn_rate_id, "id")), 4), \
        "Repair B-Check price value recalculated incorrectly!!"


def fill_in_repair_lead_b_check(driver):
    value = data.repair_lead_b_check_id
    text = '14'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair Lead B Check Value!"
    assert additional.get_property_value(driver, data.repair_delivery_b_check_id, "id") == text, "Delivery b-check value recalculated incorrectly!"


def fill_in_avg_repair_cost(driver):
    value = data.repair_avg_repair_cost_id
    text = '25'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Avg Repair Cost Value!"
    assert float(additional.get_property_value(driver, data.repair_avg_repair_price_id, "id")) == \
           round(float(additional.get_property_value(driver, value, "id")) / float(
               additional.get_property_value(driver, data.rfq_pn_rate_id, "id")), 4), \
        "Avg Repair price value recalculated incorrectly!!"
    assert additional.get_property_value(driver, data.repair_mgm_id, "id") == "-1.85", "MGM Value recalculated incorrectly!!"


def fill_in_max_repair_cost(driver):
    value = data.repair_max_cost_id
    text = '30'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Max Repair Value!"
    assert float(additional.get_property_value(driver, data.repair_max_price_id, "id")) == \
           round(float(additional.get_property_value(driver, value, "id")) / float(
               additional.get_property_value(driver, data.rfq_pn_rate_id, "id")), 4)


def fill_in_repair_lead_time(driver):
    value = data.repair_lead_time_id
    text = '7'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair Lead Time Value!"
    assert additional.get_property_value(driver, data.repair_delivery_time_id, "id") == text, "Repair Delivery Time value recalculated incorrectly!"


def fill_in_repair_qty(driver):
    value = data.repair_qty_id
    text = '10'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair Qty Value!"


def fill_in_repair_bcheck_price(driver):
    value = data.repair_b_check_price_id
    text = '12'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair B-Check Price Value!"


def fill_in_repair_delivery_b_check(driver):
    value = data.repair_delivery_b_check_id
    text = '12'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair Delivery B-Check Value!"


def fill_in_avg_repair_price(driver):
    value = data.repair_avg_repair_price_id
    text = '7'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Avg Repair Price Value!"
    assert additional.get_property_value(driver, data.repair_b_check_price_id, "id") == "7.0028", "Repair B-Check Price Value recalculated incorrectly!"
    assert additional.get_property_value(driver, data.repair_max_price_id,
                                         "id") == "8.4034", "Repair Max Price Value recalculated incorrectly!"
    assert additional.get_property_value(driver, data.repair_mgm_id,
                                         "id") == "-18.00", "Repair MGM Value recalculated incorrectly!"
    assert additional.get_property_value(driver, data.repair_mgm_percent_id,
                                         "id") == "-72.00", "Repair MGM Percent Value recalculated incorrectly!"


def fill_in_max_repair_price(driver):
    value = data.repair_max_price_id
    text = '25'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.ID, value).send_keys(Keys.ENTER)
    assert additional.get_property_value(driver, value, "id") == text + ".0000", "Wrong Repair Max Price Value!"


def fill_in_repair_delivery_time(driver):
    value = data.repair_delivery_time_id
    text = '14'
    additional.fill_text_field(driver, value, text)
    assert additional.get_property_value(driver, value, "id") == text, "Wrong Repair Delivery Time Value!"


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

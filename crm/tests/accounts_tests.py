from crm.data import authorization_data as auth_data, accounts_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# ------------------ Account Details ------------------


def select_accounts(driver):
    if driver.title != "Accounts":
        additional.wait_element_for_click(driver, auth_data.accounts_main_button_id)
        # driver.find_element(By.ID, auth_data.accounts_main_button_id).click()
    assert "Accounts", driver.title


def click_add_account(driver, url):
    additional.wait_element(driver, data.add_account_id, 'id')
    driver.find_element(By.ID, data.add_account_id).click()
    assert (url + data.expected_url) == driver.current_url and ("Accounts", driver.title)


def fill_account_name(driver, url):
    value = data.account_name_id
    text = "Autotest Account"
    additional.fill_text_field(driver, value, text)


# def website(driver):
#     value = data.website_id
#     text = "website"
#     additional.fill_text_field(driver, value, text)


def fill_ticker_symbol(driver):
    value = data.ticker_symbol_id
    text = "Autotest Ticker Symbol"
    additional.fill_text_field(driver, value, text)


def fill_in_member_of(driver):
    element_id = data.member_of_id
    additional.select_first_cell(driver, element_id, False)
    #additional.wait_element(driver, data.overwrite_dialog_no, 'xpath')
    time.sleep(2)
    additional.select_element_with_text_from_list(driver, data.overwrite_dialog_no, "xpath", "No")


def fill_fleet_size(driver):
    value = data.fleet_size_id
    text = "10"
    additional.fill_text_field(driver, value, text)


def fill_secondary_email(driver):
    value = data.secondary_email_id
    text = "wd@fas.dsa"
    additional.fill_text_field(driver, value, text)


def select_industry(driver):
    value = data.industry_id
    text = data.default_dropdown_value
    additional.select_value_from_dropdown(driver, value, text)


def select_type(driver):
    value = data.type_id
    text = data.default_dropdown_value
    # additional.select_value_from_dropdown(driver, value, text)
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def check_email_opt_out(driver):
    value = data.email_opt_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def select_assigned_to(driver):
    value = data.assigned_to_id
    text = data.assigned_to_admin
    additional.select_value_from_dropdown(driver, value, text)


def fill_account_number(driver):
    value = data.account_number_id
    text = "123"
    additional.fill_text_field(driver, value, text)


def fill_primary_phone(driver):
    value = data.primary_phone_id
    text = "123421412"
    additional.fill_text_field(driver, value, text)


def fill_fax(driver):
    value = data.fax_id
    text = "2415112"
    additional.fill_text_field(driver, value, text)


def fill_secondary_phone(driver):
    value = data.secondary_phone_id
    text = "5129321312"
    additional.fill_text_field(driver, value, text)


def fill_primary_email(driver):
    value = data.primary_email_id
    text = "asd@dsa.casd"
    additional.fill_text_field(driver, value, text)


def fill_ownership(driver):
    value = data.ownership_id
    text = "124"
    additional.fill_text_field(driver, value, text)


def select_rating(driver):
    value = data.rating_id
    text = data.default_dropdown_value
    # additional.select_value_from_dropdown(driver, value, text)
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def fill_sic_code(driver):
    value = data.sic_code_id
    text = "51231"
    additional.fill_text_field(driver, value, text)


def fill_annual_revenue(driver):
    value = data.annual_revenue_id
    text = "4500"
    additional.fill_text_field(driver, value, text)


def check_notify_owner(driver):
    value = data.notify_owner_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


# ------------------ Custom Information ------------------


def check_sync_to_qb(driver):
    value = data.sync_to_qb_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def select_qb_customer_type(driver):
    value = data.qb_customer_type_id
    text = data.default_dropdown_value
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def check_sent_to_qb(driver):
    value = data.sent_to_qb_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


def check_taxable(driver):
    value = data.taxable_id
    additional.wait_element(driver, value, 'id')
    additional.click_element_by_id(driver, value)


# ------------------ Pricing Information ------------------

def fill_tear_1_max(driver):
    value = data.tear_1_max_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_2_max(driver):
    value = data.tear_2_max_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_3_max(driver):
    value = data.tear_3_max_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_4_max(driver):
    value = data.tear_4_max_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_1_ratio(driver):
    value = data.tear_1_ratio_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_2_ratio(driver):
    value = data.tear_2_ratio_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_3_ratio(driver):
    value = data.tear_3_ratio_id
    text = "450"
    additional.fill_text_field(driver, value, text)


def fill_tear_4_ratio(driver):
    value = data.tear_4_ratio_id
    text = "450"
    additional.fill_text_field(driver, value, text)


# ------------------ Custom Information ------------------


def select_qb_company(driver):
    value = data.qb_company_id
    text = data.default_dropdown_value
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def select_terms_of_delivery(driver):
    value = data.terms_of_delivery_id
    text = data.default_dropdown_value
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def fill_recieved_via(driver):
    value = data.recieved_via_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def select_terms_of_sale(driver):
    value = data.terms_of_sale_id
    text = data.default_dropdown_value
    additional.select_element_with_text_from_list(driver, value, 'id', text)


def fill_place_of_delivery(driver):
    value = data.place_of_delivery_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def select_territory(driver):
    value = data.territory_id
    text = data.default_dropdown_value
    additional.select_element_with_text_from_list(driver, value, 'id', text)


# ------------------ Address Details ------------------


def fill_billing_address(driver):
    value = data.billing_address_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_billing_po_box(driver):
    value = data.billing_po_box_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_billing_city(driver):
    value = data.billing_city_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_billing_state(driver):
    value = data.billing_state_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_billing_postal_code(driver):
    value = data.billing_postal_code_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_billing_country(driver):
    value = data.billing_country_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_address(driver):
    value = data.shipping_address_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_po_box(driver):
    value = data.shipping_po_box_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_city(driver):
    value = data.shipping_city_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_state(driver):
    value = data.shipping_state_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_postal_code(driver):
    value = data.shipping_postal_code_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


def fill_shipping_country(driver):
    value = data.shipping_country_id
    text = "TEST DATA"
    additional.fill_text_field(driver, value, text)


# ------------------ Description Details ------------------


def fill_description(driver):
    value = data.description_id
    text = "Autotest Description"
    additional.fill_text_field(driver, value, text)


def click_save_account(driver):
    driver.execute_script("window.scrollTo(0, 0)")
    value = data.save_button
    text = "Save"
    additional.select_element_with_text_from_list(driver, value, 'xpath', text)
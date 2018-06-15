import portal.data.authorization_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
import time


def open_url(driver, url):
    driver.get(url)
    driver.find_element(By.ID, data.page)
    assert ("BAI : Welcome to BAI, Inc", driver.title)


def open_login_form(driver):
    driver.find_element(By.ID, data.login_menu_button_id).click()


def add_field(driver, value, field):
    username_field = driver.find_element(By.ID, field)
    username_field.clear()
    username_field.send_keys(value)


def add_credentials(driver, username, password):
    time.sleep(1)
    # additional.fill_text_field(driver, username, data.username_field_id)
    add_field(driver, username, data.username_field_id)
    add_field(driver, password, data.password_id)


def submit_form(driver):
    additional.wait_element(driver, data.submit, 'xpath')
    time.sleep(5)
    driver.find_element(By.XPATH, data.submit).click()


def verify_url(driver, url):
    additional.wait_element(driver, data.rfq_menu_tab, 'xpath')
    assert (url + data.expected_url) == driver.current_url and ("BAI My RFQs", driver.title)


def new_rfq(driver):
    additional.click_element_by_id(driver, data.new_rfq_id)


def fill_step_one(driver):
    additional.fill_text_field(driver, data.add_part_field_id, "PSE-173")
    additional.click_element_by_id(driver, data.step_one_next_id)


def fill_step_two(driver):
    additional.click_element_by_xpath(driver, data.step_two_chkbx)
    additional.click_element_by_id(driver, data.step_two_next_id)


def fill_step_three(driver):
    additional.fill_text_field(driver, data.step_three_description_id, "Autotest_rfq")
    additional.fill_text_field(driver, data.step_three_qty_id, "1")
    additional.click_element_by_id(driver, data.step_three_create_rfq_id)


def open_quotes_tab(driver, url):
    additional.click_element_by_xpath(driver, data.quotes_menu_tab)
    additional.wait_element(driver, data.quote_number_filter_id, "id")
    assert (url + data.quotes_expected_url) == driver.current_url and ("BAI My Quotes", driver.title)


def open_orders_tab(driver, url):
    additional.click_element_by_xpath(driver, data.orders_menu_tab)
    additional.wait_element(driver, data.order_number_filter_id, "id")
    assert (url + data.orders_expected_url) == driver.current_url and ("BAI Salesorder", driver.title)


def open_profile_tab(driver, url):
    additional.click_element_by_xpath(driver, data.profile_menu_tab)
    additional.wait_element(driver, data.ci_user_name, "xpath")
    additional.wait_element(driver, data.contact_information_tab, "xpath")
    assert (url + data.profile_expected_url) == driver.current_url


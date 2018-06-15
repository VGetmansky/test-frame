from crm.data import authorization_data as auth_data, rfq_to_po_data as wfdata
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def select_auth_data():
    additional.change_data_file("auth")


def select_rfq_data():
    additional.change_data_file("rfq")


def select_quote_data():
    additional.change_data_file("quote")


def select_so_data():
    additional.change_data_file("so")


def select_po_data():
    additional.change_data_file("po")


def click_add_quote(driver):
    driver.find_element(By.ID, wfdata.rfq_create_quote_id).click()


def click_add_so(driver):
    driver.find_element(By.ID, wfdata.quote_generate_so_id).click()


def click_add_po(driver):
    driver.find_element(By.ID, wfdata.so_generate_po_id).click()
    driver.find_element(By.XPATH, wfdata.create_po).click()

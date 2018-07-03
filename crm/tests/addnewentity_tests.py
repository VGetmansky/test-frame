import crm.data.rfq_to_po_data as rfq_to_po_data
from selenium.webdriver.common.by import By
import common_functions as additional


def test_click_add_quote_from_rfq(driver):
    additional.wait_element(driver, rfq_to_po_data.rfq_create_quote_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.rfq_create_quote_id).click()
    additional.wait_element(driver, rfq_to_po_data.save_button_id, 'id')
    additional.wait_element(driver, rfq_to_po_data.quote_account_id, 'id')


def test_click_add_so_from_quote(driver):
    additional.wait_element(driver, rfq_to_po_data.quote_generate_so_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.quote_generate_so_id).click()
    additional.wait_element(driver, rfq_to_po_data.create_quote_button, "xpath")
    driver.find_element(By.XPATH, rfq_to_po_data.create_quote_button).click()
    additional.wait_element(driver, rfq_to_po_data.save_button_id, 'id')


def test_click_add_po_from_so(driver):
    additional.wait_element(driver, rfq_to_po_data.so_generate_po_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.so_generate_po_id).click()
    additional.wait_element(driver, rfq_to_po_data.create_quote_button, "xpath")
    driver.find_element(By.XPATH, rfq_to_po_data.create_quote_button).click()


def click_open_po(driver, url):
    additional.wait_element(driver, rfq_to_po_data.po_cell_id, "id")
    additional.select_table_cell(driver, "PurchaseOrder_listView_row_1", "po", url)


def click_open_so(driver, url):
    additional.wait_element(driver, rfq_to_po_data.so_cell_id, "id")
    additional.select_table_cell(driver, "SalesOrder_listView_row_1", "so", url)

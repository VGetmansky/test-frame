import crm.data.rfq_to_po_data as rfq_to_po_data
from selenium.webdriver.common.by import By
import common_functions as additional


def test_click_add_quote_from_rfq(driver):
    new_url = driver.current_url
    additional.wait_element(driver, rfq_to_po_data.rfq_create_quote_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.rfq_create_quote_id).click()
    additional.wait_element(driver, rfq_to_po_data.save_button_id, 'id')
    additional.wait_element(driver, rfq_to_po_data.quote_account_id, 'id')
    additional.wait_new_page(driver, new_url)


def test_click_add_so_from_quote(driver):
    new_url = driver.current_url
    additional.wait_element(driver, rfq_to_po_data.quote_generate_so_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.quote_generate_so_id).click()
    # bool(driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[8].size == {'height': 20.0, 'width': 20.0})
    additional.check_all_item_checkbuttons(driver)
    additional.wait_element(driver, rfq_to_po_data.create_quote_button, "xpath")
    driver.find_element(By.XPATH, rfq_to_po_data.create_quote_button).click()
    additional.wait_element(driver, rfq_to_po_data.save_button_id, 'id')
    additional.wait_new_page(driver, new_url)


def test_click_add_po_from_so(driver):
    new_url = driver.current_url
    additional.wait_element(driver, rfq_to_po_data.so_generate_po_id, "id")
    driver.find_element(By.ID, rfq_to_po_data.so_generate_po_id).click()
    additional.wait_element(driver, rfq_to_po_data.create_quote_button, "xpath")
    driver.find_element(By.XPATH, rfq_to_po_data.create_quote_button).click()
    additional.wait_new_page(driver, new_url)


def click_open_po(driver, url):
    new_url = driver.current_url
    additional.wait_element(driver, rfq_to_po_data.po_cell_id, "id")
    additional.select_table_cell(driver, "PurchaseOrder_listView_row_1", "po", url)
    additional.wait_new_page(driver, new_url)


def click_open_so(driver, url):
    additional.wait_element(driver, rfq_to_po_data.so_cell_id, "id")
    additional.select_table_cell(driver, "SalesOrder_listView_row_1", "so", url)

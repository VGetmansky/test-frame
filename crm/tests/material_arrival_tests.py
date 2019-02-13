from crm.data import authorization_data as auth_data, material_arrival_data as data
from selenium.webdriver.common.by import By
import common_functions as additional
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, re

from selenium.webdriver.common.keys import Keys


def click_all_category(driver):
    additional.select_category_all(driver)


def select_material_arrival_category(driver, url):
    additional.wait_element(driver, data.material_arrival_id, 'id')
    # driver.find_element(By.ID, data.material_arrival_id).click()
    driver.find_elements(By.ID, data.material_arrival_id)[1].click()
    assert (url + data.material_arrival_expected_url) == driver.current_url and ("WHStock", driver.title)


def open_qatest_url(driver):
    driver.get("http://crmqa.bai-inc.eu/crmqa/#/shipping/arrival")
    assert ("Shipping: Material Arrival", driver.title)


def select_vendor(driver):
    value = data.vendor_select_id
    # text = data.autotest_vendor
    # additional.select_value_from_dropdown(driver, value, text)
    element_id = value

    additional.wait_element(driver, element_id, 'id')
    driver.find_element(By.ID, element_id).click()

    elem = driver.find_element(By.ID, value)
    text = "Autotest User"
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, value)))

    additional.wait_element(driver, value, 'id')
    time.sleep(1)
    driver.find_element(By.ID, value).click()
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)

    time.sleep(1)
    # additional.wait_element(driver, value, 'xpath')
    driver.find_element(By.XPATH,data.autotest_vendor).click()


def select_po(driver, ponum):
    value = data.po_select_id
    text = ponum
    element = '//li[contains(., "' + ponum +'")]'
    additional.fill_text_field(driver, value, text)
    driver.find_element(By.XPATH, element).click()

    driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')[
        len(driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')) - 1]


def get_last_po_number_from_list(driver):
    driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')[
        len(driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')) - 1].text.split('\n')[0]


def expand_po_list(driver):
    while len(driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')) == 0:
        time.sleep(0.1)
    time.sleep(1)
    driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')[
        len(driver.find_elements(By.XPATH, '//div[@class="collapse-block-header-in"]')) - 1].click()

    # if type == "PO":
    #     driver.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')[0].click()
    # else:
    #     None


def check_all_ma_partnumbers(driver, type):
    if type == "PO":
        driver.find_elements(By.XPATH, data.ma_checkbox)[0].click()
    else:
        None


def filter_by_last_po(driver):
    value = data.po_filter_id
    additional.select_last_element_from_list(driver, value)


def check_po_checkboxes(driver):
    value = data.material_arrival_checkboxes
    additional.check_all_item_checkbuttonspo(driver, value)


def fill_arrived_qty(driver):
    i = 0
    for i in range(0, len(driver.find_elements(By.XPATH, '//input[contains(@id, "arrival-arrived-0-")]'))):
        value = "ma_arrived_" + str(i) + "_id"
        value = getattr(data, value)
        text = "3"
        additional.fill_text_field(driver, value, text)
        i += 1


def select_shipping_notice_category(driver, url):
    additional.wait_element(driver, data.shipping_notice_id, 'id')
    driver.find_elements(By.ID, data.shipping_notice_id)[1].click()
    assert (url + data.shipping_notice_expected_url) == driver.current_url and ("WHStock", driver.title)


def select_account(driver):
    value = data.select_account_id
    text = data.autotest_account
    additional.select_value_from_dropdown(driver, value, text)


def filter_by_last_so(driver):
    value = data.so_filter_id
    additional.wait_element(driver, value, 'id')
    additional.select_last_element_from_list(driver, value)


def filter_add_note(driver):
    value = data.notes_id
    text = "Autotest Filled Notes"
    additional.fill_text_field(driver, value, text)


def check_shipping_notice_so_checkboxes(driver):
    value = data.material_arrival_checkboxes
    additional.check_all_item_checkbuttonspo(driver, value)


def select_inspection_category(driver, url):
    additional.wait_element(driver, data.inspection_id, 'id')
    driver.find_elements(By.ID, data.inspection_id)[1].click()
    assert (url + data.inspection_expected_url) == driver.current_url and ("WHStock", driver.title)


def filter_by_last_inspection(driver, page):
    value = data.inspection_select_id
    additional.select_last_material_arrival_inspection(driver, value, page)


def select_all_material_arrival_inspection(driver):
    value = data.select_all_button_id
    driver.find_element(By.ID, value).click()
    driver.find_element(By.ID, value).click()


def select_receiving(driver, url):
    additional.wait_element(driver, data.receiving_id, 'id')
    driver.find_elements(By.ID, data.receiving_id)[1].click()
    assert (url + data.receiving_expected_url) == driver.current_url and ("WHStock", driver.title)


def select_all_material_arrival_chkboxes(driver):
    value = data.select_all_button_id
    driver.find_element(By.ID, value).click()


def select_packing(driver, url):
    additional.wait_element(driver, data.packing_id, 'id')
    driver.find_elements(By.ID, data.packing_id)[1].click()
    assert (url + data.receiving_expected_url) == driver.current_url and ("WHStock", driver.title)


def fill_material_arrival_warehouse_index(driver):
    text = "2"
    value = data.isle_id
    additional.fill_text_field(driver, value, text)
    value = data.shelf_id
    additional.fill_text_field(driver, value, text)
    value = data.holder_id
    additional.fill_text_field(driver, value, text)


def click_material_arrival_deliver(driver):
    url_before = driver.current_url
    driver.find_element(By.ID, data.deliver_button_id).click()
    url_after = driver.current_url
    while url_before == url_after:
        time.sleep(1)
        url_after = driver.current_url
    else:
        assert data.ma_test_history_url == driver.current_url and ("Shipping: Arrival History", driver.title)


def click_material_arrival_send_notice(driver):
    additional.click_material_arrival_buttons(driver, data.send_notice_button)


def click_material_arrival_approve(driver):
    additional.click_material_arrival_buttons(driver, data.approve_button)


def click_material_arrival_receive(driver):
    additional.click_material_arrival_buttons(driver, data.receive_button)
    assert driver.current_url == "http://crmqa.bai-inc.eu/crmqa/#/shipping/arrival/history"


def click_material_arrival_notice(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # additional.wait_element(driver, data.ah_notice_id)
    driver.find_element(By.ID, data.ah_notice_id).click()
    assert driver.current_url == "http://crmqa.bai-inc.eu/crmqa/#/shipping/notice"


def click_material_arrival_inspection(driver):
    driver.find_element(By.ID, data.ah_inspection_id).click()
    assert driver.current_url == "http://crmqa.bai-inc.eu/crmqa/#/shipping/notice"


def get_newest_po_number(driver):
    driver.find_elements(By.XPATH, '//div[@class="sh-title-item"]')[len(driver.find_elements(By.XPATH, '//div[@class="sh-title-item"]')) - 1].text


def check_delivered_material_arrival(driver):
    # assert data.ma_arrived_x_id == ma_arrived_x
    return None

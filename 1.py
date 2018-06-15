import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://crmtst_us.bai-inc.eu/")
        self.assertIn("Users", driver.title)
        elem = driver.find_element_by_name("username")
        elem.send_keys("vladislav.getmanskiy@zimad.com")
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_name("password")
        elem.send_keys("Welcome2018!")
        assert "No results found." not in driver.page_source

        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        if driver.title == "Home":
            elem = driver.find_element_by_id("menubar_item_Rfq")
            elem.click()

        if driver.title == "Rfq":
            elem = driver.find_element_by_id("Rfq_listView_basicAction_LBL_ADD_RECORD")
            elem.click()

        windowHandler = driver.window_handles
        # window_before = driver.window_handles[0]
        #
        # elem = driver.find_element_by_id("vendor_searh")
        # elem.click()
        #
        # WebDriverWait(driver, 10).until(
        #     lambda driver: len(windowHandler) != len(self.driver.window_handles))
        #
        # window_after = driver.window_handles[1]
        # driver.switch_to.window(window_after)
        #
        # wait = WebDriverWait(driver, 10)
        # elem = wait.until(EC.element_to_be_clickable((By.ID, "Vendors_popUpListView_row_1")))
        #
        # builder = ActionChains(driver)
        # builder.move_to_element(elem).click(elem).perform()
        #
        # driver.switch_to.window(window_before)

        #using self waiter
        #wait = additionalFunc.wait(elem)


        wait = WebDriverWait(driver, 15)
        elem = wait.until((EC.element_to_be_clickable((By.XPATH, '//div[@class="add-line-button line-button pull-left"]'))))
        elem.click()

        listel = driver.find_elements_by_xpath('//input[@name="Button" and @value="Insert]')

        # elem = driver.find_element_by_xpath('//div[@class="add-line-button line-button pull-left"]').click()
        #listel = driver.find_elements_by_xpath('//input[ @id="" and @class="standart-input-inputitem d_pn" and @type="text"]')
        #elem = driver.find_element_by_xpath('//input[@class="standart-input-inputitem d_pn" and @type="text"]')

        listel[2].click()
        actions = ActionChains(driver)
        actions.move_to_element(elem).click().send_keys('1')
        #driver.find_element_by_xpath('//input[@value="input"]').click()
        driver.find_element_by_xpath('//input[@name="Button" and @value="Insert"]').click()

        # elem.send_keys("1")

        time.sleep(30)

    def tearDown(self):
        self.driver.close()

# class additionalFunc():
#     def wait(self, elem):
#         i = 0
#         while i < 3:
#             try:
#                 elem.click()
#             except Exception:
#                 print("")
#
#             i=i+1


if __name__ == "__main__":
    unittest.main()

time.sleep(30)

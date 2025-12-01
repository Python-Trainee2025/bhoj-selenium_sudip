import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_obj.search.search_properties import SearchProperties
from page_obj.search.search_locators import SearchLocators


class SearchPage(SearchProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def search_item(self, food, expected=None):

        # 1: Wait until search box is clickable (using locator)
        self.wait.until(EC.element_to_be_clickable(SearchLocators.SEARCH_BOX))

        # 2: Now interact through WebElement property
        searchbox = self.search_input
        searchbox.clear()
        searchbox.send_keys(food)

        # Wait for suggestions to appear
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='main-auto-suggestion']"))
        )

        # If expected value is provided → click matching suggestion
        if expected:
            expected_locator = (
                By.XPATH,
                f"//span[contains(translate(normalize-space(), "
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
                f"'{expected.lower()}')]"
            )

            item = self.wait.until(EC.element_to_be_clickable(expected_locator))
            item.click()
            logging.info(f"Clicked expected result: {expected}")

        else:
            # Else → click first suggestion
            first_item = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='main-auto-suggestion']//span)[1]"))
            )
            first_item.click()



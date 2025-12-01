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
        logging.info("SearchPage initialized")

    def search_item(self, food, expected=None):
        logging.info(f"Starting search for: {food}")

        # Wait for search box
        logging.info("Waiting for SEARCH_BOX to be clickable")
        self.wait.until(EC.element_to_be_clickable(SearchLocators.SEARCH_BOX))

        # Interact using property
        searchbox = self.search_input
        logging.info("Clearing search box")
        searchbox.clear()

        logging.info(f"Typing search query: {food}")
        searchbox.send_keys(food)

        # Wait for suggestions
        logging.info("Waiting for search suggestions to appear")
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='main-auto-suggestion']"))
        )

        # If expected item is provided
        if expected:
            logging.info(f"Looking for expected suggestion: {expected}")

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
            logging.info("No expected value provided. Clicking first suggestion.")
            first_item = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='main-auto-suggestion']//span)[1]"))
            )
            first_item.click()

        logging.info("Search operation completed successfully")

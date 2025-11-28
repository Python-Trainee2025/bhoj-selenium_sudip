from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .filter_locators import FilterLocators

class FilterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def complete_filter_flow(self):

        # Step 1: Click first button
        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.FIRST_BUTTON)
        ).click()

        # Step 2: Click popup image
        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.POPUP_SELECT)
        ).click()

        # Step 3: Sort dropdown -> option 3
        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.SORT_DROPDOWN)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.SORT_OPTION_3)
        ).click()

        # Step 4: Filter dropdown -> option 3
        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.FILTER_DROPDOWN)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(FilterLocators.FILTER_OPTION_3)
        ).click()

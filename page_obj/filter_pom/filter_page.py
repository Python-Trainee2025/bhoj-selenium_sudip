import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from page_obj.filter_pom.filter_properties import FilterProperties
from page_obj.filter_pom.filter_locators import FilterLocators


class FilterPage(FilterProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        logging.info("FilterPage initialized")

    # APPLY FILTERS

    def apply_todays_deal(self):
        logging.info("Waiting for Today's Deal filter to be clickable")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.TODAY_DEAL))
        self.todays_deal_btn.click()
        logging.info("Today's Deal filter applied")

    def apply_category(self):
        logging.info("Waiting for Category filter button to be clickable")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.BROWSE_CATEGORY))
        self.category_btn.click()
        logging.info("Category filter applied")

    def apply_cuisine(self):
        logging.info("Waiting for Cuisine filter button to be clickable")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.BROWSE_CUISINE))
        self.cuisine_btn.click()
        logging.info("Cuisine filter applied")

    # SORTING

    def sort_by_popularity(self):
        logging.info("Sorting by Popularity")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.SORT_POPULARITY))
        select = Select(self.popularity_sort)
        select.select_by_value("lowtohigh")
        self.popularity_sort.send_keys(Keys.ESCAPE)
        logging.info("Sorted by popularity")

    def sort_by_price(self):
        logging.info("Sorting by Price")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.SORT_PRICE))
        select = Select(self.price_sort)
        select.select_by_value("3")
        self.price_sort.send_keys(Keys.ESCAPE)
        logging.info("Sorted by price")

    # OTHER ACTIONS

    def open_all_restaurants(self):
        logging.info("Opening All Restaurants")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.ALL_RESTAURANT))
        self.all_restaurants_btn.click()
        logging.info("All Restaurants opened")

    def reset_filters(self):
        logging.info("Resetting all filters")
        self.wait.until(EC.element_to_be_clickable(FilterLocators.RESET))
        self.reset_button.click()
        logging.info("Filters reset successfully")

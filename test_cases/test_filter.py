import time
import logging

from page_obj.login.login_page import LoginPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.search.search_page import SearchPage
from page_obj.filter_pom.filter_page import FilterPage
from setup.base_test import BaseTest


class TestFilter(BaseTest):

    def test_filter_functions(self):
        logging.info(" Starting Filter Test")

        # 1. Open base URL
        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        # 2. Login
        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        logging.info(f"Logging in with email: {uname}")
        login.login(uname, pwd)

        # 3. Select Location
        logging.info("Selecting location")
        getlocation = GetLocationPage(self.driver)
        getlocation.get_location_page()

        # 4. Searching
        # logging.info("Searching item")
        # search = SearchPage(self.driver)
        # search.search_item("burger", "the burger house and crunchy fried chicken")
        # time.sleep(3)

        # 5. Create Filter Page object
        logging.info("Initializing FilterPage")
        filter = FilterPage(self.driver)
        time.sleep(10)

        # Apply filters
        logging.info("Applying Today's Deal filter")
        filter.apply_todays_deal()
        time.sleep(10)

        logging.info("Applying Category filter")
        filter.apply_category()
        time.sleep(10)

        logging.info("Applying Cuisine filter")
        filter.apply_cuisine()
        time.sleep(10)

        # Sorting
        logging.info("Sorting by popularity")
        filter.sort_by_popularity()
        time.sleep(5)

        logging.info("Sorting by price")
        filter.sort_by_price()
        time.sleep(5)

        # Open All Restaurants
        logging.info("Opening all restaurants")
        filter.open_all_restaurants()
        time.sleep(5)

        # Reset Filters
        logging.info("Resetting all filters")
        filter.reset_filters()
        time.sleep(10)

        logging.info("Filter Test Completed Successfully")

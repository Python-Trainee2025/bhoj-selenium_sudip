import time
import logging

from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from setup.base_test import BaseTest


class TestSearch(BaseTest):

    def test_search(self):
        logging.info(" Starting Search Test ")

        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        logging.info(f"Attempting login with email: {uname}")
        login.login(uname, pwd)
        logging.info("Login successful")

        getlocation = GetLocationPage(self.driver)
        logging.info("Selecting user location")
        getlocation.get_location_page()

        logging.info("Initializing SearchPage")
        search = SearchPage(self.driver)

        logging.info("Searching for: 'burger'")
        search.search_item("burger", "The Burger House and Crunchy Fried Chicken (Pepsicola)")

        logging.info("Search action complete")
        time.sleep(8)

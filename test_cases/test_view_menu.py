import logging
import time

from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from page_obj.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest


class TestViewMenu(BaseTest):

    def test_view_menu(self):
        logging.info(" Starting View Menu Test ")

        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        logging.info("Initializing LoginPage")
        login = LoginPage(self.driver)

        uname = self.cred["email"]
        pwd = self.cred["password"]
        logging.info(f"Logging in with: {uname}")
        login.login(uname, pwd)

        logging.info("Selecting delivery location")
        location = GetLocationPage(self.driver)
        location.get_location_page()
        time.sleep(5)

        logging.info("Searching for menu item: burger")
        search = SearchPage(self.driver)
        search.search_item("burger", "The Burger House and Crunchy Fried Chicken (Pepsicola)")
        time.sleep(10)

        logging.info("Opening View Menu Page")
        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        logging.info("View Menu page opened successfully")
        time.sleep(10)

        logging.info("View Menu Test Completed ")

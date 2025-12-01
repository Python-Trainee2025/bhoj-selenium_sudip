
import logging
import time

from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from page_obj.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestViewMenu(BaseTest):

    def test_view_menu(self):
        url=self.cred["base_url"]
        self.driver.get(url)

        login=LoginPage(self.driver)
        uname=self.cred["email"]
        pwd=self.cred["password"]
        login.login(uname,pwd)

        location=GetLocationPage(self.driver)
        location.get_location_page()
        time.sleep(5)

        search=SearchPage(self.driver)
        search.search_item("burger","The Burger House and Crunchy Fried Chicken (Pepsicola)")
        time.sleep(10)

        view_menu=ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        logging.info("View menu page")
        time.sleep(10)

import logging
import time

from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from setup.base_test import BaseTest


class TestGetLocation(BaseTest):
    def test_get_location(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")

        loginpage = LoginPage(self.driver)
        email = self.cred["email"]
        logging.info("Email entered")

        pwd = self.cred["password"]
        logging.info("Password entered")
        loginpage.login(email, pwd)
        time.sleep(3)

        getlocation_p=GetLocationPage(self.driver)
        getlocation_p.get_location_page()
        time.sleep(3)
import logging
import time

from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from setup.base_test import BaseTest


class TestGetLocation(BaseTest):
    def test_get_location(self):
        logging.info("Starting Get Location Test")

        url = self.cred["base_url"] #url stores link from dictationary in base test
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        logging.info("Initializing LoginPage")
        loginpage = LoginPage(self.driver)

        email = self.cred["email"]
        logging.info(f"Email entered: {email}")

        pwd = self.cred["password"]
        logging.info("Password entered")
        loginpage.login(email, pwd)
        time.sleep(3)

        logging.info("Initializing GetLocationPage")
        getlocation = GetLocationPage(self.driver)

        logging.info("Selecting location")
        getlocation.get_location_page()
        time.sleep(3)

        logging.info("Get Location Test Completed")

import time
import logging
from setup.base_test import BaseTest
from page_obj.login.login_page  import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        logging.info("Starting login test")

        # Open the site using BaseTest method
        logging.info("Opening URL https://www.bhojdeals.com/")
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)
        logging.info("LoginPage object initialized")

        # Use credentials stored inside BaseTest
        logging.info(f"Attempting login with email={self.email}")
        login.login(self.email, self.password)

        logging.info("Login test completed")

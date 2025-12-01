import time
import logging
from setup.base_test import BaseTest
from page_obj.login.login_page import LoginPage


class TestLogin(BaseTest):

    def test_invalid_login(self):
        logging.info("Starting Invalid Login Test")

        logging.info("Opening Bhojdeals URL")
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        logging.info("Initializing LoginPage")
        login = LoginPage(self.driver)

        invalid_email = "wrong@mail.com"
        invalid_pass = "wrongPass123"
        logging.info(f"Attempting login with invalid credentials: {invalid_email}")

        login.login(invalid_email, invalid_pass)

        logging.info("Fetching error message after invalid login attempt")
        error = login.get_error_message()

        assert error is not None, "Expected an error message but got None"
        logging.info(f"Error message displayed: {error}")

        logging.info(" Invalid Login Test Completed ")

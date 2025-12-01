import time
import logging
from setup.base_test import BaseTest
from page_obj.login.login_page import LoginPage


class TestLogout(BaseTest):

    def test_logout(self):
        logging.info(" Starting Logout Test")

        logging.info("Opening Bhojdeals homepage")
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        logging.info("Initializing LoginPage")
        login = LoginPage(self.driver)

        # Step 1: Login
        logging.info(f"Logging in with email: {self.email}")
        login.login(self.email, self.password)
        time.sleep(3)
        logging.info("Login successful")

        # Step 2: Logout
        logging.info("Attempting logout")
        login.logout()
        time.sleep(2)
        logging.info("Logout action executed")

        # Step 3: Validate logout
        logging.info("Validating logout state")
        assert login.nav_login_btn.is_displayed(), "Login button should appear after logout"
        logging.info("Logout successful!")

        logging.info(" Logout Test Completed Successfully")

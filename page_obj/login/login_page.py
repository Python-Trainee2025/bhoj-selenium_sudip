import time
import logging
from page_obj.login.login_properties  import LoginProperties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver
        logging.info("LoginPage initialized")

    def login(self, email, password):

        logging.info("Starting login process")
        time.sleep(2)

        # Try clicking navbar login button ONLY if it exists
        try:
            logging.info("Trying to click navbar login button")
            self.nav_login_btn.click()
            time.sleep(2)
        except Exception as e:
            logging.warning(f"Navbar login button not clickable or already on login page: {e}")

        #  Now fill the login form (works in both cases)
        try:
            logging.info("Clearing email field")
            self.email.clear()
        except:
            logging.warning("Email field not clearable")

        logging.info(f"Entering email: {email}")
        self.email.send_keys(email)
        time.sleep(1)

        try:
            logging.info("Clearing password field")
            self.password.clear()
        except:
            logging.warning("Password field not clearable")

        logging.info("Entering password")
        self.password.send_keys(password)
        time.sleep(1)

        logging.info("Clicking login submit button")
        self.submit_btn.click()
        time.sleep(3)

        logging.info("Login process finished")

    def get_error_message(self):
        """Returns login error message if exists."""
        logging.info("Checking for login error message")
        try:
            return self.error_message.text.strip()
        except NoSuchElementException:
            logging.info("No login error message found")
            return None

    def logout(self):
        logging.info("Attempting logout")
        time.sleep(2)
        self.logout_btn.click()
        time.sleep(2)
        logging.info("Logout completed")

    def open_forgot_password(self):
        logging.info("Opening forgot password page")
        time.sleep(2)
        self.forgot_password_link.click()
        time.sleep(2)

    def open_my_account(self):
        logging.info("Opening My Account page")
        time.sleep(2)
        self.my_account_btn.click()
        time.sleep(3)

    def open_edit_profile(self):
        logging.info("Opening Edit Profile page")
        time.sleep(2)
        self.edit_profile_btn.click()
        time.sleep(10)

    def edit_username(self, new_name):
        logging.info(f"Editing profile username to: {new_name}")
        time.sleep(10)
        self.profile_username_input.clear()
        time.sleep(10)
        self.profile_username_input.send_keys(new_name)
        time.sleep(10)

    def submit_profile(self):
        logging.info("Submitting profile changes")
        time.sleep(2)
        self.profile_submit_btn.click()
        time.sleep(3)

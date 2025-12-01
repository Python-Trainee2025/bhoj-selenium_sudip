import time
from page_obj.login.login_properties  import LoginProperties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException




class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):

        time.sleep(2)

        # Try clicking navbar login button ONLY if it exists
        try:
            self.nav_login_btn.click()
            time.sleep(2)
        except:
            #  Already on /login page → do nothing
            pass

        #  Now fill the login form (works in both cases)
        try:
            self.email.clear()
        except:
            pass

        self.email.send_keys(email)
        time.sleep(1)

        try:
            self.password.clear()
        except:
            pass

        self.password.send_keys(password)
        time.sleep(1)

        self.submit_btn.click()
        time.sleep(3)

    def get_error_message(self):
        """Returns login error message if exists."""
        try:
            return self.error_message.text.strip()
        except NoSuchElementException:
            return None

    def logout(self):
        time.sleep(2)
        self.logout_btn.click()
        time.sleep(2)

    def open_forgot_password(self):
        time.sleep(2)
        self.forgot_password_link.click()
        time.sleep(2)

    def open_my_account(self):
        time.sleep(2)
        self.my_account_btn.click()
        time.sleep(3)

    def open_edit_profile(self):
        time.sleep(2)
        self.edit_profile_btn.click()
        time.sleep(10)

    def edit_username(self, new_name):
        time.sleep(10)
        self.profile_username_input.clear()
        time.sleep(10)
        self.profile_username_input.send_keys(new_name)
        time.sleep(10)

    def submit_profile(self):
        time.sleep(2)
        self.profile_submit_btn.click()
        time.sleep(3)

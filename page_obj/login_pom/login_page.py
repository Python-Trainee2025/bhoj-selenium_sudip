import time
from page_obj.login_pom.login_properties  import LoginProperties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException




class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        time.sleep(3)
        self.nav_login_btn.click()
        time.sleep(2)

        self.email.send_keys(email)
        time.sleep(1)

        self.password.send_keys(password)
        time.sleep(1)

        self.submit_btn.click()
        time.sleep(5)

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
        time.sleep(3)

    def edit_username(self, new_name):
        time.sleep(2)
        self.profile_username_input.clear()
        time.sleep(1)
        self.profile_username_input.send_keys(new_name)
        time.sleep(1)

    def submit_profile(self):
        time.sleep(2)
        self.profile_submit_btn.click()
        time.sleep(3)

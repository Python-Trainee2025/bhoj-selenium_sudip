import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page  import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        # Open the site using BaseTest method
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

        # Use credentials stored inside BaseTest
        login.login(self.email, self.password)
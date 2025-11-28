import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage


class TestUIElements(BaseTest):

    def test_login_button_visible(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

        assert login.nav_login_btn.is_displayed(), "Login button is NOT visible"

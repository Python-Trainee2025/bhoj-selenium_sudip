import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage


class TestForgotPassword(BaseTest):

    def test_forgot_password_link(self):
        # Step 1: Open site
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

        # Step 2: Click login button on navbar
        login.nav_login_btn.click()
        time.sleep(2)

        # Step 3: Click Forgot Password
        login.open_forgot_password()
        time.sleep(2)

        # Step 4: Validate page opens (URL should contain "forgot")
        assert "forgot" in self.driver.current_url.lower(), "Forgot Password page did NOT open!"

        print("Forgot Password page opened successfully!")

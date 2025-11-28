import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage


class TestLogout(BaseTest):

    def test_logout(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        login = LoginPage(self.driver)

        # Step 1: Login
        login.login(self.email, self.password)
        time.sleep(3)

        # Step 2: Logout
        login.logout()
        time.sleep(2)

        # Step 3: Validate logout
        assert login.nav_login_btn.is_displayed(), "Login button should appear after logout"
        print("Logout successful!")

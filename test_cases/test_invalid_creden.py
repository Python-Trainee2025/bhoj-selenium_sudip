import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage


class TestLogin(BaseTest):

    def test_invalid_login(self):
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(2)

        login = LoginPage(self.driver)

        login.login("projetc@mail.com", "wrongPass123")

        error = login.get_error_message()

        assert error is not None
        print("Error:", error)

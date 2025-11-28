import time
from setup.base_test import BaseTest
from page_obj.login_pom.login_page import LoginPage
from page_obj.filter_pom.filter_page import FilterPage


class TestFilterFlow(BaseTest):

    def test_filter_flow(self):
        # Open site
        self.open_url("https://www.bhojdeals.com/")
        time.sleep(3)

        # Login first
        login = LoginPage(self.driver)
        login.login(self.email, self.password)
        time.sleep(5)

        # Now run filter flow
        filter_flow = FilterPage(self.driver)
        filter_flow.complete_filter_flow()

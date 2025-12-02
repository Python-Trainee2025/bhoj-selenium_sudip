import time
from page_obj.get_location.getlocation_page  import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from setup.base_test import BaseTest


class TestSearch (BaseTest):
    def test_search(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        login.login(uname,pwd)

        getlocation = GetLocationPage(self.driver)
        getlocation.get_location_page()

        search = SearchPage(self.driver)
        search.search_item("burger","The Burger House and Crunchy Fried Chicken (Pepsicola)")
        time.sleep(3)
import time

from page_obj.login.login_page import LoginPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.search.search_page import SearchPage
from page_obj.filter_pom.filter_page import FilterPage
from setup.base_test import BaseTest


class TestFilter(BaseTest):

    def test_filter_functions(self):
        # 1. Open base URL
        url = self.cred["base_url"]
        self.driver.get(url)

        # 2. Login
        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        login.login(uname, pwd)

        # 3. Select Location
        getlocation = GetLocationPage(self.driver)
        getlocation.get_location_page()

        # 4. Must perform a search first
       # search = SearchPage(self.driver)
        #search.search_item("burger", "the burger house and crunchy fried chicken")
        #time.sleep(3)

        # 5. Use new Filter Page
        filter = FilterPage(self.driver)
        time.sleep(10)

        # Apply filters
        filter.apply_todays_deal()
        time.sleep(10)

        filter.apply_category()
        time.sleep(10)

        filter.apply_cuisine()
        time.sleep(10)

        # Sorting
        filter.sort_by_popularity()
        time.sleep(5)

        filter.sort_by_price()
        time.sleep(5)

        # Open All Restaurants
        filter.open_all_restaurants()
        time.sleep(5)

        # Reset Filters
        filter.reset_filters()
        time.sleep(10)

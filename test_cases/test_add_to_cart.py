import logging
import time

from page_obj.add_to_cart.add_to_cart_page import AddToCartPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from page_obj.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest


class TestAddToCart(BaseTest):
    def test_add_to_cart(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")

        loginpage = LoginPage(self.driver)
        email = self.cred["email"]
        pwd = self.cred["password"]
        loginpage.login(email,pwd)
        logging.info("Login successful")
        time.sleep(3)

        getlocation_p=GetLocationPage(self.driver)
        getlocation_p.get_location_page()
        time.sleep(3)

        search = SearchPage(self.driver)
        search.search_item("burger","The Burger House and Crunchy Fried Chicken (Pepsicola)")
        time.sleep(3)

        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        time.sleep(9)

        add_cart=AddToCartPage(self.driver)
        add_cart.add_to_cart_page()
        time.sleep(9)
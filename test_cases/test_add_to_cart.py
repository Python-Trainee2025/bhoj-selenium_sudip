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
        logging.info("Starting Add to Cart Test")

        url = self.cred["base_url"]
        logging.info(f"Opening base URL: {url}")
        self.driver.get(url)
        logging.info("Driver initialized")

        loginpage = LoginPage(self.driver)
        email = self.cred["email"]
        pwd = self.cred["password"]
        logging.info(f"Attempting login with email: {email}")
        loginpage.login(email, pwd)
        logging.info("Login successful")
        time.sleep(3)

        logging.info("Going to Get Location page")
        getlocation_p = GetLocationPage(self.driver)
        getlocation_p.get_location_page()
        time.sleep(3)

        logging.info("Performing search for burger")
        search = SearchPage(self.driver)
        search.search_item("burger", "The Burger House and Crunchy Fried Chicken (Pepsicola)")
        time.sleep(3)

        logging.info("Opening menu page")
        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        time.sleep(5)

        logging.info("Adding items to car")
        add_cart = AddToCartPage(self.driver)
        add_cart.add_to_cart_page()
        logging.info("Add to Cart process complete")
        time.sleep(5)

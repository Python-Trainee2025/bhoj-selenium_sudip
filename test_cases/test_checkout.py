import logging
import time
from page_obj.add_to_cart.add_to_cart_page import AddToCartPage
from page_obj.checkout.checkout_page import CheckoutPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from page_obj.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest


class TestCheckout(BaseTest):
    def test_checkout(self):

        logging.info(" Starting Checkout Test")

        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)
        logging.info("Driver initialized")
        time.sleep(3)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        logging.info(f"Logging in with: {uname}")
        login.login(uname, pwd)
        logging.info("Login successful")

        location = GetLocationPage(self.driver)
        logging.info("Selecting location")
        location.get_location_page()
        time.sleep(3)
        logging.info("Location selected")

        logging.info("Searching for product: amore pizza")
        search = SearchPage(self.driver)
        search.search_item("amore pizza", "Amore Pizza (Koteshwor)")
        time.sleep(3)
        logging.info("Search complete")

        logging.info("Opening menu page")
        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        time.sleep(3)

        logging.info("Adding items to cart")
        add_cart = AddToCartPage(self.driver)
        add_cart.add_to_cart_page()
        time.sleep(3)

        logging.info("Proceeding to checkout")
        checkout = CheckoutPage(self.driver)
        checkout.checkout_page("Budhanilkantha,Chapali", "JUST TESTING")
        logging.info("Checkout completed successfully")
        time.sleep(3)

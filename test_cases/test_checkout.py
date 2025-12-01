import logging
import time
from page_obj.add_to_cart.add_to_cart_page   import AddToCartPage
from page_obj.checkout.checkout_page import CheckoutPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.login.login_page import LoginPage
from page_obj.search.search_page import SearchPage
from page_obj.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout(BaseTest):
    def test_checkout(self):

        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")
        time.sleep(3)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        login.login(uname, pwd)
        logging.info("Successful Login")

        location = GetLocationPage(self.driver)
        location.get_location_page()
        time.sleep(3)
        logging.info("got location")

        search=SearchPage(self.driver)
        search.search_item("amore pizza","Amore Pizza (Koteshwor)")
        time.sleep(3)
        logging.info("search product")

        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        logging.info("View menu page")
        time.sleep(3)

        add_cart = AddToCartPage(self.driver)
        add_cart.add_to_cart_page()
        time.sleep(3)

        checkout=CheckoutPage(self.driver)
        checkout.checkout_page("Budhanilkantha,Chapali","JUST TESTING")
        time.sleep(3)
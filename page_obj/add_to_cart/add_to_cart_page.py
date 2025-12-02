import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_obj.add_to_cart.add_to_cart_properties import AddToCartProperties
from page_obj.add_to_cart.add_to_cart_locaters import AddToCartLocators


class AddToCartPage(AddToCartProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        logging.info("AddToCartPage initialized")

    def add_to_cart_page(self):
        logging.info("Waiting for first item to be clickable")

        firstitem = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.FIRST_ITEM)
        )
        logging.info("Clicking first item")
        firstitem.click()

        logging.info("Waiting for second item to be clickable")
        seconditem = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.SECOND_ITEM)
        )
        logging.info("Clicking second item")
        seconditem.click()

        logging.info("Increasing item quantity")
        add_quantity = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.ADD_QUANTITY)
        )
        add_quantity.click()  #click variablenamee

        logging.info("Reducing item quantity")
        sub_quantity = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.SUBTRACT_QUANTITY)
        )
        sub_quantity.click()

        logging.info("Add to Cart actions completed")

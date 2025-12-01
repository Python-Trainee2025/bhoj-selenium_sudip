from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_obj.add_to_cart.add_to_cart_properties import AddToCartProperties
from page_obj.add_to_cart.add_to_cart_locaters import AddToCartLocators


class AddToCartPage(AddToCartProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart_page(self):


        firstitem = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.FIRST_ITEM)
        )
        firstitem.click()


        seconditem = self.wait.until(
            EC.element_to_be_clickable(AddToCartLocators.SECOND_ITEM)
        )
        seconditem.click()

        add_quantity = self.wait.until( EC.element_to_be_clickable(AddToCartLocators.ADD_QUANTITY)
        )
        add_quantity.click()

        sub_quantity = self.wait.until(EC.element_to_be_clickable(AddToCartLocators.SUBTRACT_QUANTITY))
        sub_quantity.click()
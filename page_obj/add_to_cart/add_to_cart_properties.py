import logging
from page_obj.add_to_cart.add_to_cart_locaters import AddToCartLocators


class AddToCartProperties(AddToCartLocators):

    @property
    def burger(self):
        logging.info("Accessing burger (FIRST_ITEM)")
        return self.driver.find_element(*AddToCartLocators.FIRST_ITEM)

    @property
    def burger(self):
        logging.info("Accessing burger (SECOND_ITEM)")
        return self.driver.find_element(*AddToCartLocators.SECOND_ITEM)

    @property
    def one_more(self):
        logging.info("Accessing + (ADD_QUANTITY)")
        return self.driver.find_element(*AddToCartLocators.ADD_QUANTITY)

    @property
    def one_less(self):
        logging.info("Accessing - (SUBTRACT_QUANTITY)")
        return self.driver.find_element(*AddToCartLocators.SUBTRACT_QUANTITY)

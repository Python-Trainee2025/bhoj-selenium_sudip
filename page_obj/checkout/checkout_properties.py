import logging
from page_obj.checkout.checkout_locaters import CheckoutLocators


class CheckoutProperties(CheckoutLocators):

    @property
    def checkout_buttonclick(self):
        logging.info("Accessing CHECKOUT_BUTTON")
        return self.driver.find_element(*CheckoutLocators.CHECKOUT_BUTTON)

    @property
    def add_delivery_button(self):
        logging.info("Accessing ADD_DELIVERY_BUTTON")
        return self.driver.find_element(*CheckoutLocators.ADD_DELIVERY_BUTTON)

    @property
    def add_delivery_address(self):
        logging.info("Accessing DELIVERY_ADDRESS")
        return self.driver.find_element(*CheckoutLocators.DELIVERY_ADDRESS)

    @property
    def close_address(self):
        logging.info("Accessing CLOSE_ADDRESS_POPUP")
        return self.driver.find_element(*CheckoutLocators.CLOSE_ADDRESS_POPUP)

    @property
    def confirm_call(self):
        logging.info("Accessing CONFIRMATION_CALL")
        return self.driver.find_element(*CheckoutLocators.CONFIRMATION_CALL)

    @property
    def delivery_day(self):
        logging.info("Accessing DELIVERY_DAY")
        return self.driver.find_element(*CheckoutLocators.DELIVERY_DAY)

    @property
    def delivery_note(self):
        logging.info("Accessing DELIVERY_NOTE")
        return self.driver.find_element(*CheckoutLocators.DELIVERY_NOTE)

    @property
    def payment_method(self):
        logging.info("Accessing PAYMENT_METHOD")
        return self.driver.find_element(*CheckoutLocators.PAYMENT_METHOD)

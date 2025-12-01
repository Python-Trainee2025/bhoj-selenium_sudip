from page_obj.checkout.checkout_locaters import CheckoutLocators


class CheckoutProperties(CheckoutLocators):


    @property
    def checkout_buttonclick(self):
        return self.driver.find_element(*CheckoutLocators.CHECKOUT_BUTTON)

    @property
    def add_delivery_button(self):
        return self.driver.find_element(*CheckoutLocators.ADD_DELIVERY_BUTTON)

    @property
    def add_delivery_address(self):
        return self.driver.find_element(*CheckoutLocators.DELIVERY_ADDRESS)

    @property
    def close_address(self):
        return self.driver.find_element(*CheckoutLocators.CLOSE_ADDRESS_POPUP)


    @property
    def confirm_call(self):
        return self.driver.find_element(*CheckoutLocators.CONFIRMATION_CALL)

    @property
    def delivery_day(self):
        return self.driver.find_element(*CheckoutLocators.DELIVERY_DAY)

    @property
    def delivery_note(self):
        return self.driver.find_element(*CheckoutLocators.DELIVERY_NOTE)

    @property
    def payment_method(self):
        return self.driver.find_element(*CheckoutLocators.PAYMENT_METHOD )
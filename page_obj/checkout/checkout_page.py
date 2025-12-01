import logging
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_obj.checkout.checkout_properties import CheckoutProperties


class CheckoutPage(CheckoutProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        logging.info("CheckoutPage initialized")

    def checkout_page(self, address, note):

        logging.info("Clicking checkout button")
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.checkout_buttonclick)
        )
        checkout_button.click()
        time.sleep(5)
        logging.info("Checkout button clicked")

        logging.info("Clicking Add Delivery Address button")
        add_delivery_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_delivery_button)
        )
        add_delivery_btn.click()
        logging.info("Add delivery button clicked")

        logging.info("Adding delivery address")
        add_address = self.add_delivery_address
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_address)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_address)
        add_address.send_keys(address)
        logging.info(f"Delivery address entered: {address}")
        time.sleep(5)

        logging.info("Closing address popup")
        close = self.close_address
        close.click()
        time.sleep(5)

        logging.info("Selecting call confirmation option")
        call_confirmation = self.wait.until(
            EC.visibility_of_element_located(self.CONFIRMATION_CALL)
        )
        call_confirmation.click()
        logging.info("Confirmation call checked")
        time.sleep(6)

        logging.info("Setting delivery day")
        delivery_time = self.delivery_day
        self.driver.execute_script("arguments[0].scrollIntoView(true);", delivery_time)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", delivery_time)
        logging.info("Delivery day set to Tomorrow")
        time.sleep(6)

        logging.info("Adding note to driver")
        extra_note = self.wait.until(EC.presence_of_element_located(self.DELIVERY_NOTE))
        extra_note.click()
        extra_note.send_keys(note)
        logging.info(f"Driver note added: {note}")

        logging.info("Selecting payment method")
        payment = self.payment_method
        payment.click()
        logging.info("Payment method selected")

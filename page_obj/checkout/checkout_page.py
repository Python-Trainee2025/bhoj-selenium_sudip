import logging
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from page_obj.checkout.checkout_properties import CheckoutProperties


class CheckoutPage(CheckoutProperties):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 10)

    def checkout_page(self,address,note):

        #checkout button click
        checkout_button = self.wait.until(
        EC.element_to_be_clickable(self.checkout_buttonclick))
        checkout_button.click()
        time.sleep(5)
        logging.info("checkout button clicked")

        #click on add delivery button
        add_delivery_btn= self.wait.until(
        EC.element_to_be_clickable(self.add_delivery_button))
        add_delivery_btn.click()
        logging.info("add delivery address button clicked ")


        add_address=self.add_delivery_address
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_address)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_address)
        add_address.send_keys(address)
        logging.info("address added")
        time.sleep(5)



        #close the address popup
        close=self.close_address
        close.click()
        time.sleep(5)

        #choose option for call for confirmation
        call_confirmation=self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_CALL))
        call_confirmation.click()
        logging.info("Call for confirmation checked")
        time.sleep(6)

        #delivery day
        delivery_time= self.delivery_day
        self.driver.execute_script("arguments[0].scrollIntoView(true);", delivery_time)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", delivery_time)
        time.sleep(6)
        logging.info("delivery day set to tomorrow")

        #note to driver
        extra_note=self.wait.until(EC.presence_of_element_located(self.DELIVERY_NOTE))
        extra_note.click()
        extra_note.send_keys(note)

        #payment method
        payment=self.payment_method
        payment.click()
        logging.info("checked on the payment method")
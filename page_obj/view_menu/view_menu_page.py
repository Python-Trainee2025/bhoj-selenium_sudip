import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_obj.view_menu.view_menu_properties import ViewMenuProperties
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class ViewMenuPage(ViewMenuProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver, 20)

    def view_menu_page(self):
        view = self.select_restaurant
        view.click()
        time.sleep(2)

        # ---- Smooth Scroll Down ----
        total_scroll = 2000  # how far down to scroll
        step = 200  # scroll amount per step
        delay = 0.3  # delay between steps

        # Scroll DOWN
        scrolled = 0
        while scrolled < total_scroll:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", step)
            time.sleep(delay)
            scrolled += step

        time.sleep(1)

        # ---- Smooth Scroll BACK TO TOP ----
        scrolled_up = 0
        while scrolled_up < total_scroll:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", -step)
            time.sleep(delay)
            scrolled_up += step

        time.sleep(1)

        # ---- Scroll a little bit DOWN again ----
        small_scroll = 300  # small scroll
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", small_scroll)
        time.sleep(1)

        logging.info("Scrolled down → back to top → small scroll completed")


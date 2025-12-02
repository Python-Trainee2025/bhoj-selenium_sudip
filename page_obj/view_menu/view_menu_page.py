import time
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_obj.view_menu.view_menu_locaters  import ViewMenuLocators

from page_obj.view_menu.view_menu_properties import ViewMenuProperties


class ViewMenuPage(ViewMenuProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        logging.info("ViewMenuPage initialized")

    def view_menu_page(self):
        logging.info("Clicking restaurant to open menu")
        view = self.select_restaurant
        view.click()
        time.sleep(2)

        # Smooth scrolling settings
        logging.info("Starting smooth scroll down")
        total_scroll = 2000
        step = 200
        delay = 0.3

        scrolled = 0
        while scrolled < total_scroll:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", step)
            time.sleep(delay)
            scrolled += step

        logging.info("Completed scrolling down; now scrolling back up")
        time.sleep(1)

        scrolled_up = 0
        while scrolled_up < total_scroll:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", -step)
            time.sleep(delay)
            scrolled_up += step

        logging.info("Scrolling up completed")
        time.sleep(1)

        logging.info("Performing small final scroll")
        small_scroll = 300
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", small_scroll)
        time.sleep(1)

        logging.info("View Menu scroll interactions completed")



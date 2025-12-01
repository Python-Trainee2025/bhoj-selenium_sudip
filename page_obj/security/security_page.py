import time
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from page_obj.security.security_properties import SecurityProperties
from page_obj.security.security_locators import SecurityLocators
from page_obj.get_location.getlocation_page import GetLocationPage


class SecurityPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.search_ready = False
        logging.info("SecurityPage initialized")


    # PREPARE SEARCH BOX

    def _prepare_search_box(self):
        logging.info("Preparing search box...")

        if self.search_ready:
            logging.info("Search box already prepared — skipping.")
            return True

        try:
            logging.info("Opening location selector...")
            gl = GetLocationPage(self.driver)
            gl.get_location_page()
            time.sleep(2)

            logging.info("Waiting for SEARCH_BOX to become visible")
            self.wait.until(
                EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
            )

            self.search_ready = True
            logging.info("Search box preparation completed")

        except Exception as e:
            logging.error(f"Search preparation failed: {e}")
            return False

        return True


    # ENTER SEARCH TEXT

    def enter_search(self, text):
        logging.info(f"Entering search text: {text}")

        if not self._prepare_search_box():
            logging.error("Search box not prepared!")
            return False

        try:
            search = self.wait.until(
                EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
            )
            search.clear()
            search.send_keys(text)
            time.sleep(1)

            logging.info("Search text entered successfully")
            return True

        except TimeoutException:
            logging.error(" Search box not found!")
            return False


    # XSS INJECTION TEST

    def test_xss_injection(self):
        logging.info("===== Starting XSS Injection Test =====")

        for payload in SecurityProperties.XSS_PAYLOADS:
            logging.info(f"--- Testing XSS Payload: {payload} ---")

            if not self.enter_search(payload):
                logging.error("Failed to enter XSS payload into search box")
                return False

            time.sleep(1)

            try:
                self.wait.until(
                    EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
                )
            except TimeoutException:
                logging.error(" XSS succeeded — page crashed or redirected!")
                return False

            logging.info(" XSS blocked successfully")

        logging.info("XSS Injection Test Passed ")
        return True


    # RATE LIMITING TEST

    def test_rate_limit(self):
        logging.info("Starting Rate Limiting Test ")
        total_attempts = SecurityProperties.RATE_LIMIT_COUNT

        for i in range(1, total_attempts + 1):
            logging.info(f"Search attempt #{i}")

            if not self.enter_search("burger"):
                logging.error(" Search attempt failed")
                return False

            time.sleep(0.6)

        logging.info("No crash — Rate limiting behavior is stable")
        logging.info("Rate Limiting Test Passed ")
        return True

import time
import random
import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from page_obj.stress_test.stress_locators import StressLocators
from page_obj.stress_test.stress_properties import StressProperties
from page_obj.get_location.getlocation_page import GetLocationPage


class StressPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.search_ready = False
        logging.info("StressPage initialized")

    # ----------------------------------------------------
    # PREPARE SEARCH BOX (Only once)
    # ----------------------------------------------------
    def _prepare_search_box(self):
        logging.info("Preparing search box...")

        if self.search_ready:
            logging.info("Search box already prepared — skipping.")
            return True

        try:
            logging.info("Selecting location via GetLocationPage")
            gl = GetLocationPage(self.driver)
            gl.get_location_page()

            self.wait.until(EC.visibility_of_element_located(StressLocators.SEARCH_BOX))
            self.search_ready = True
            logging.info("Search box ready")

            return True

        except Exception as e:
            logging.error(f" Search preparation failed: {e}")
            return False


    # PERFORM ONE SEARCH

    def _perform_search(self, keyword):
        logging.info(f"Performing search with keyword: {keyword}")

        if not self._prepare_search_box():
            logging.error("Search box preparation failed")
            return False

        try:
            search = self.wait.until(
                EC.visibility_of_element_located(StressLocators.SEARCH_BOX)
            )

            search.clear()
            search.send_keys(keyword)

            start = time.time()
            self.wait.until(
                EC.visibility_of_element_located(StressLocators.SEARCH_RESULTS)
            )
            response_time = time.time() - start

            logging.info(f"Search response time: {response_time:.2f}s")

            if response_time > StressProperties.MAX_RESPONSE_TIME:
                logging.warning(f"Slow response detected: {response_time:.2f}s")

            return True

        except TimeoutException:
            logging.error(" Search failed — no results found")
            return False


    # REPEATED SEARCH STRESS TEST

    def repeated_search_stress(self):
        logging.info("=== Running Repeated Search Stress Test ===")

        for i in range(StressProperties.TOTAL_REQUESTS):
            keyword = random.choice(StressProperties.RANDOM_KEYWORDS)
            logging.info(f"[Request #{i+1}] Searching for: {keyword}")

            if not self._perform_search(keyword):
                logging.error("Page unstable during repeated stress test")
                return False

            delay = random.uniform(StressProperties.MIN_DELAY, StressProperties.MAX_DELAY)
            logging.info(f"Sleeping for {delay:.2f}s before next request")
            time.sleep(delay)

        logging.info(" Repeated Search Stress Test completed successfully")
        return True


    # HIGH LOAD USER SIMULATION

    def high_load_user_simulation(self):
        logging.info("=== Running High Load User Simulation ===")

        for i in range(30):
            keyword = random.choice(StressProperties.RANDOM_KEYWORDS)
            logging.info(f"[User Simulation #{i+1}] Searching for: {keyword}")

            if not self._perform_search(keyword):
                logging.error(" High-load search failed")
                return False

            delay = random.uniform(0.5, 1.5)
            logging.info(f"Simulating user wait time: {delay:.2f}s")
            time.sleep(delay)

        logging.info(" High-load user simulation completed successfully")
        return True

import time
import random
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

    def _prepare_search_box(self):
        """
        Prepares search bar ONCE, just like in previous tests.
        Uses GetLocationPage.get_location_page() as in your project.
        """
        if self.search_ready:
            return True

        try:
            gl = GetLocationPage(self.driver)
            gl.get_location_page()   # SAME METHOD YOU ALREADY USE

            # wait for search box
            self.wait.until(
                EC.visibility_of_element_located(StressLocators.SEARCH_BOX)
            )

            self.search_ready = True
            return True

        except Exception as e:
            print(f"❌ Search preparation failed: {e}")
            return False

    def _perform_search(self, keyword):
        """Performs one search and measures response time."""
        if not self._prepare_search_box():
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

            if response_time > StressProperties.MAX_RESPONSE_TIME:
                print(f"⚠ Slow response: {response_time:.2f}s")

            return True

        except TimeoutException:
            print("❌ Search failed — no results found")
            return False

    def repeated_search_stress(self):
        """Fast repeated searching."""
        print("=== Running Repeated Search Stress Test ===")

        for i in range(StressProperties.TOTAL_REQUESTS):
            keyword = random.choice(StressProperties.RANDOM_KEYWORDS)
            print(f"Request #{i+1} — Searching: {keyword}")

            if not self._perform_search(keyword):
                print("❌ Page unstable during stress test")
                return False

            time.sleep(random.uniform(
                StressProperties.MIN_DELAY,
                StressProperties.MAX_DELAY
            ))

        print("✔ Stress test completed successfully")
        return True

    def high_load_user_simulation(self):
        """Simulates natural heavy user activity."""
        print("=== Running High Load User Simulation ===")

        for i in range(30):
            keyword = random.choice(StressProperties.RANDOM_KEYWORDS)
            print(f"[User] Searching: {keyword}")

            if not self._perform_search(keyword):
                print("❌ High-load search failed")
                return False

            time.sleep(random.uniform(0.5, 1.5))

        print("✔ High-load simulation successful")
        return True

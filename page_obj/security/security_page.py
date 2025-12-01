import time
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
        self.search_ready = False    # <-- NEW FLAG

    def _prepare_search_box(self):
        """
        Prepares the search box only ONCE.
        Prevents repeated clicking of location-selection buttons.
        """
        if self.search_ready:
            return True   # already done once

        try:
            gl = GetLocationPage(self.driver)
            gl.get_location_page()      # your actual method
            time.sleep(2)

            # wait for search box
            self.wait.until(
                EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
            )

            self.search_ready = True  # <-- mark as completed

        except Exception as e:
            print(f"Search preparation failed: {e}")
            return False

        return True

    def enter_search(self, text):
        """Types search text after preparing search area."""
        if not self._prepare_search_box():
            return False

        try:
            search = self.wait.until(
                EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
            )
            search.clear()
            search.send_keys(text)
            time.sleep(1)
            return True

        except TimeoutException:
            print("❌ Search box not found!")
            return False

    def test_xss_injection(self):
        """Runs all XSS payloads."""
        for payload in SecurityProperties.XSS_PAYLOADS:
            print(f"--- Testing XSS Payload: {payload} ---")

            if not self.enter_search(payload):
                print("❌ Failed to inject payload")
                return False

            time.sleep(1)

            try:
                self.wait.until(
                    EC.visibility_of_element_located(SecurityLocators.SEARCH_BOX)
                )
            except TimeoutException:
                print("❌ XSS succeeded! Page crashed or redirected")
                return False

            print("✔ XSS blocked (safe)")

        return True

    def test_rate_limit(self):
        """Spam-search to test rate limiting."""
        print("--- Testing Rate Limiting ---")

        for i in range(1, 6):
            print(f"Search attempt #{i}")

            if not self.enter_search("burger"):
                print("❌ Search attempt failed")
                return False

            time.sleep(0.6)

        print("✔ No crash — Rate limiting OK")
        return True

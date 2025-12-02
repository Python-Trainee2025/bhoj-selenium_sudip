import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_obj.stress_test.stress_locators import SearchStressRandomLocators
from page_obj.stress_test.stress_properties import SearchStressRandomProperties


class SearchStressRandomPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.info("SearchStressRandomPage initialized")

    def run_random_stress_test(self):
        search_box = self.wait.until(
            EC.element_to_be_clickable(SearchStressRandomLocators.SEARCH_BOX)
        )

        # Generate 120 random words
        random_words = SearchStressRandomProperties.generate_random_words()

        logging.info(f"Generated {len(random_words)} random words for stress test")

        success_count = 0

        for word in random_words:
            search_box.clear()
            search_box.send_keys(word)
            logging.info(f"Typed: {word}")

            time.sleep(0.10)  # very fast input

            # Check if suggestions appear without needing correctness
            try:
                self.wait.until(
                    EC.presence_of_all_elements_located(SearchStressRandomLocators.SEARCH_SUGGESTIONS)
                )
                success_count += 1
            except:
                pass

        return success_count, len(random_words)

import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_obj.stress_test.stress_locators import SearchStressLocators
from page_obj.stress_test.stress_properties  import SearchStressProperties


class SearchStressWordsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.info("SearchStressWordsPage initialized")

    def run_stress_test(self):
        search_box = self.wait.until(
            EC.element_to_be_clickable(SearchStressLocators.SEARCH_BOX)
        )

        predefined_words = SearchStressProperties.PREDEFINED_WORDS
        total = len(predefined_words)
        success_count = 0

        logging.info(f"Running stress test using {total} predefined words")

        for word in predefined_words:
            search_box.clear()
            search_box.send_keys(word)
            logging.info(f"Typed: {word}")

            time.sleep(0.10)  # rapid typing (100ms)

            # Check suggestion UI appears
            try:
                self.wait.until(
                    EC.presence_of_all_elements_located(SearchStressLocators.SEARCH_SUGGESTIONS)
                )
                success_count += 1
            except:
                pass

        return success_count, total

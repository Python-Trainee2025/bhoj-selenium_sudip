import time
import logging
from setup.base_test import BaseTest

from page_obj.login.login_page import LoginPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.stress_test.stress_page import SearchStressWordsPage


class TestSearchStressWords(BaseTest):

    def test_predefined_word_stress_search(self):

        logging.info("Starting predefined-word search stress test")

        # Step 1 — open website
        self.open_url(self.cred["base_url"])
        time.sleep(3)

        # Step 2 — login
        login = LoginPage(self.driver)
        login.login(self.email, self.password)
        time.sleep(3)

        # Step 3 — select location
        location = GetLocationPage(self.driver)
        location.get_location_page()
        time.sleep(3)

        # Step 4 — run stress test
        stress = SearchStressWordsPage(self.driver)
        success, total = stress.run_stress_test()

        logging.info(f"Suggestions appeared for {success}/{total} words")

        # At least 70% words should produce suggestions
        assert success >= (total * 0.70), "Search suggestions failed frequently!"

        logging.info("Predefined-word stress test completed successfully")

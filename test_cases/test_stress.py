import logging
import time
from setup.base_test import BaseTest
from page_obj.login.login_page import LoginPage
from page_obj.get_location.getlocation_page import GetLocationPage
from page_obj.stress_test.stress_page import SearchStressRandomPage


class TestSearchStressRandom(BaseTest):

    def test_random_word_stress_search(self):
        logging.info("Starting random search stress test")

        # Step 1: Open URL
        self.open_url(self.cred["base_url"])
        time.sleep(3)

        # Step 2: Login
        login = LoginPage(self.driver)
        login.login(self.email, self.password)
        time.sleep(3)

        # Step 3: Select location
        location = GetLocationPage(self.driver)
        location.get_location_page()
        time.sleep(3)

        # Step 4: Stress test
        stress = SearchStressRandomPage(self.driver)
        success, total = stress.run_random_stress_test()

        logging.info(f"Suggestions appeared for {success}/{total} random inputs")

        assert success >= (total * 0.60), "Search suggestions failed frequently during stress test!"  # 60% threshold

        logging.info("Random word stress test completed successfully")

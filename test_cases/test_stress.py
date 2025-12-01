import logging
from setup.base_test import BaseTest
from page_obj.stress_test.stress_page import StressPage


class TestStress(BaseTest):

    def test_repeated_search_stress(self):
        logging.info(" Starting Repeated Search Stress Test ")
        self.driver.get(self.cred["base_url"])
        sp = StressPage(self.driver)
        assert sp.repeated_search_stress(), "Repeated Search Stress Test FAILED"
        logging.info(" Repeated Search Stress Test Completed Successfully ")

    def test_high_load_user_simulation(self):
        logging.info(" Starting High Load User Simulation Test ")
        self.driver.get(self.cred["base_url"])
        sp = StressPage(self.driver)
        assert sp.high_load_user_simulation(), "High Load User Simulation FAILED"
        logging.info(" High Load User Simulation Completed Successfully ")

from setup.base_test import BaseTest
from page_obj.stress_test.stress_page import StressPage


class TestStress(BaseTest):

    def test_repeated_search_stress(self):
        self.driver.get(self.cred["base_url"])
        sp = StressPage(self.driver)
        assert sp.repeated_search_stress(), "Repeated Search Stress Test FAILED"

    def test_high_load_user_simulation(self):
        self.driver.get(self.cred["base_url"])
        sp = StressPage(self.driver)
        assert sp.high_load_user_simulation(), "High Load User Simulation FAILED"

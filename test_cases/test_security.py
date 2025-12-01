import logging
import pytest
from page_obj.security.security_page import SecurityPage
from setup.base_test import BaseTest


class TestSecurity(BaseTest):

    def test_xss_injection(self):
        logging.info(" Starting XSS Injection Test")
        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        sp = SecurityPage(self.driver)
        assert sp.test_xss_injection(), "XSS Injection test FAILED!"
        logging.info(" XSS Injection Test Completed Successfully ")

    def test_rate_limiting(self):
        logging.info(" Starting Rate Limiting Test ")
        url = self.cred["base_url"]
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

        sp = SecurityPage(self.driver)
        assert sp.test_rate_limit(), "Rate limiting test FAILED!"
        logging.info("Rate Limiting Test Completed Successfully ")

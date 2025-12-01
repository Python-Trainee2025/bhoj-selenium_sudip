import pytest
from page_obj.security.security_page import SecurityPage
from setup.base_test import BaseTest


class TestSecurity(BaseTest):


    def test_xss_injection(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        sp = SecurityPage(self.driver)
        assert sp.test_xss_injection(), "XSS Injection test FAILED!"

    def test_rate_limiting(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        sp = SecurityPage(self.driver)
        assert sp.test_rate_limit(), "Rate limiting test FAILED!"

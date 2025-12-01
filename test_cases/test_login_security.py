from setup.base_test import BaseTest
from page_obj.login_security.login_security_page import LoginSecurityPage


class TestLoginSecurity(BaseTest):

    def test_sql_injection(self):
        self.driver.get(self.cred["base_url"])     # go to homepage

        sec = LoginSecurityPage(self.driver)
        assert sec.test_sql_injection(self.email), "SQL Injection FAILED!"

    def test_bruteforce_login(self):
        self.driver.get(self.cred["base_url"])     # go to homepage
        sec = LoginSecurityPage(self.driver)
        assert sec.test_brute_force(self.email), "Brute Force Protection FAILED!"

import logging
from setup.base_test import BaseTest
from page_obj.login_security.login_security_page import LoginSecurityPage


class TestLoginSecurity(BaseTest):

    def test_sql_injection(self):
        logging.info(" Starting SQL Injection Security Test")
        self.driver.get(self.cred["base_url"])
        sec = LoginSecurityPage(self.driver)

        assert sec.test_sql_injection(self.email), "SQL Injection FAILED!"
        logging.info(" SQL Injection Test Completed Successfully ")

    def test_bruteforce_login(self):
        logging.info("Starting Brute Force Security Test ")
        self.driver.get(self.cred["base_url"])
        sec = LoginSecurityPage(self.driver)

        assert sec.test_brute_force(self.email), "Brute Force Protection FAILED!"
        logging.info(" Brute Force Test Completed Successfully ")

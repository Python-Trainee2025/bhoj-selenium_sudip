import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_obj.login.login_page import LoginPage
from .login_security_locators import LoginSecurityLocators
from .login_security_properties import LoginSecurityProperties


class LoginSecurityPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.info("LoginSecurityPage initialized")


    # Shared Login Function

    def attempt_login(self, email, password):
        logging.info(f"Attempting login with email={email}, password={password}")
        login = LoginPage(self.driver)
        login.login(email, password)
        time.sleep(2)
        logging.info("Login attempt completed")


    # SQL Injection Test

    def test_sql_injection(self, valid_email):

        logging.info(" Starting SQL Injection Test ")

        for payload in LoginSecurityProperties.SQL_PAYLOADS:

            logging.info(f"Testing SQL payload: {payload}")

            self.attempt_login(valid_email, payload)

            # If login unexpectedly succeeds then FAIL
            if "/my-account" in self.driver.current_url.lower():
                logging.error(f"CRITICAL: Login succeeded with SQL payload: {payload}")
                return False

            # Check if error message is shown
            try:
                self.wait.until(
                    EC.visibility_of_element_located(LoginSecurityLocators.ERROR_MESSAGE)
                )
                logging.info(" Error message displayed — SQL injection blocked")
            except:
                # If still on login page, still safe
                if "login" in self.driver.current_url.lower():
                    logging.warning("No error visible, but login prevented (still safe)")
                    continue

                logging.error(f" SQL Injection payload NOT blocked: {payload}")
                return False

        logging.info(" SQL Injection Test Passed ")
        return True



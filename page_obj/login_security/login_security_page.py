import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_obj.login.login_page import LoginPage
from .login_security_locators import LoginSecurityLocators
from .login_security_properties import LoginSecurityProperties


class LoginSecurityPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Reuse working login page
    def attempt_login(self, email, password):
        login = LoginPage(self.driver)
        login.login(email, password)
        time.sleep(2)

    # ------------------------------------
    # SQL Injection Test (with debug)
    # ------------------------------------
    def test_sql_injection(self, valid_email):

        for payload in LoginSecurityProperties.SQL_PAYLOADS:

            print(f"\n--- Testing SQL payload: {payload} ---")

            self.attempt_login(valid_email, payload)

            # If login succeeds → FAIL immediately
            if "/my-account" in self.driver.current_url.lower():
                print(f"Login succeeded with SQL payload: {payload}")
                return False

            # Check for error message
            try:
                self.wait.until(
                    EC.visibility_of_element_located(LoginSecurityLocators.ERROR_MESSAGE)
                )
                print("✔ Error message displayed (safe)")
            except:
                # No error message, but still on login page → still safe
                if "login" in self.driver.current_url.lower():
                    print("⚠ No visible error message, but login blocked (still safe)")
                    continue

                # Anything else = unsafe
                print(f"❌ SQL payload failed: {payload}")
                return False

        return True

    # ------------------------------------
    # Brute Force Test
    # ------------------------------------
    def test_brute_force(self, target_email):

        for attempt, pwd in enumerate(LoginSecurityProperties.BRUTE_FORCE_PASSWORDS, start=1):

            print(f"Attempt {attempt}: Password = {pwd}")
            self.attempt_login(target_email, pwd)

            try:
                self.wait.until(
                    EC.visibility_of_element_located(LoginSecurityLocators.ERROR_MESSAGE)
                )
                print("✔ Wrong password rejected")
            except:
                print(" Wrong password accepted!")
                return False

            if attempt >= LoginSecurityProperties.MAX_BRUTE_FORCE_ATTEMPTS:
                break

        return True

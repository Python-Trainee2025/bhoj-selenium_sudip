import logging
from selenium.webdriver.common.by import By


class LoginSecurityLocators:
    logging.info("LoginSecurityLocators loaded")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-dismissible.alert-danger")

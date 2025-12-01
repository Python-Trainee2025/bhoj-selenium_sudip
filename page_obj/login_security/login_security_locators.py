from selenium.webdriver.common.by import By

class LoginSecurityLocators:
    # Your website shows errors inside Bootstrap alert-danger box
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-dismissible.alert-danger")

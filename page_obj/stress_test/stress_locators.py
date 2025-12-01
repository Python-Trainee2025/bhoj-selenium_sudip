import logging
from selenium.webdriver.common.by import By


class StressLocators:
    logging.info("StressLocators loaded")

    SEARCH_BOX = (By.ID, "exampleInput1")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".mb-3")

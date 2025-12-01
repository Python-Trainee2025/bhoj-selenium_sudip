import logging
from selenium.webdriver.common.by import By


class GetLocationLocators(object):
    logging.info("GetLocationLocators loaded")

    GETLOCATION = (By.XPATH, "//h2[normalize-space()='Get Food & Grocery delivered']")
    LOCATION_KTM_PATAN = (By.XPATH, "//img[@title='Kathmandu and Lalitpur']")
    LOCATION_BHAKTAPUR = (By.XPATH, "//img[@title='Bhaktapur']")

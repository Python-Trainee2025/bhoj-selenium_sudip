import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_obj.get_location.getlocation_properties import GetLocationProperties


class GetLocationPage(GetLocationProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        logging.info("GetLocationPage initialized")

    def get_location_page(self):
        logging.info("Waiting for 'Get Food & Grocery delivered' section")
        get_location_page = self.wait.until(
            EC.presence_of_element_located(self.GETLOCATION) #Just check if the element exists in the page’s HTML.
        ) # here get_location_page is a variable

        logging.info("Clicking main Get Location button")
        get_location_page.click()

        logging.info("Selecting specific location (Bhaktapur)")
        choose_location = self.chooselocation
        choose_location.click()

        logging.info("Location successfully selected")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_obj.get_location.getlocation_properties import GetLocationProperties

from selenium.webdriver.support import expected_conditions as EC
class GetLocationPage(GetLocationProperties):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def get_location_page(self):
        get_location_page=self.wait.until(EC.presence_of_element_located(self.GETLOCATION))
        get_location_page.click()

        choose_location=self.chooselocation
        choose_location.click()
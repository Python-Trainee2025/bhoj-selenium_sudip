import logging
from page_obj.get_location.getlocation_locators import GetLocationLocators


class GetLocationProperties(GetLocationLocators):

    @property
    def getlocation(self):
        logging.info("Locating main 'Get Location' button")
        return self.driver.find_element(*GetLocationLocators.GETLOCATION)

    @property
    def chooselocation(self):
        logging.info("Locating Bhaktapur location option")
        return self.driver.find_element(*GetLocationLocators.LOCATION_BHAKTAPUR)

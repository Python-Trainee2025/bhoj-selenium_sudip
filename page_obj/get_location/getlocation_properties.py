from page_obj.get_location.getlocation_locators import GetLocationLocators


class GetLocationProperties(GetLocationLocators):

    @property
    def getlocation(self):
        return self.driver.find_element(*GetLocationLocators.GETLOCATION)

    @property
    def chooselocation(self):
        return self.driver.find_element(*GetLocationLocators.LOCATION_BHAKTAPUR)
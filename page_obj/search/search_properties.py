import logging
from page_obj.search.search_locators import SearchLocators


class SearchProperties:
    @property
    def search_input(self):
        logging.info("Accessing SEARCH_BOX element")
        return self.driver.find_element(*SearchLocators.SEARCH_BOX)

    @property
    def dropdown_click(self):
        logging.info("Accessing DROPDOWN element")
        return self.driver.find_element(*SearchLocators.DROPDOWN)

    @property
    def dropdown_items(self):
        logging.info("Accessing DROPDOWN_ITEMS list")
        return self.driver.find_elements(*SearchLocators.DROPDOWN_ITEMS)

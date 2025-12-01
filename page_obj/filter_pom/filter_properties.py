import logging
from page_obj.filter_pom.filter_locators import FilterLocators


class FilterProperties:

    @property
    def todays_deal_btn(self):
        logging.info("Accessing TODAY_DEAL button")
        return self.driver.find_element(*FilterLocators.TODAY_DEAL)

    @property
    def category_btn(self):
        logging.info("Accessing BROWSE_CATEGORY button")
        return self.driver.find_element(*FilterLocators.BROWSE_CATEGORY)

    @property
    def cuisine_btn(self):
        logging.info("Accessing BROWSE_CUISINE button")
        return self.driver.find_element(*FilterLocators.BROWSE_CUISINE)

    @property
    def popularity_sort(self):
        logging.info("Accessing SORT_POPULARITY dropdown")
        return self.driver.find_element(*FilterLocators.SORT_POPULARITY)

    @property
    def price_sort(self):
        logging.info("Accessing SORT_PRICE dropdown")
        return self.driver.find_element(*FilterLocators.SORT_PRICE)

    @property
    def all_restaurants_btn(self):
        logging.info("Accessing ALL_RESTAURANT button")
        return self.driver.find_element(*FilterLocators.ALL_RESTAURANT)

    @property
    def reset_button(self):
        logging.info("Accessing RESET button")
        return self.driver.find_element(*FilterLocators.RESET)

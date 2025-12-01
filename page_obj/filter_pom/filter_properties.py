# page_obj/filter/filter_properties.py
from page_obj.filter_pom.filter_locators import FilterLocators

class FilterProperties:

    @property
    def todays_deal_btn(self):
        return self.driver.find_element(*FilterLocators.TODAY_DEAL)

    @property
    def category_btn(self):
        return self.driver.find_element(*FilterLocators.BROWSE_CATEGORY)

    @property
    def cuisine_btn(self):
        return self.driver.find_element(*FilterLocators.BROWSE_CUISINE)

    @property
    def popularity_sort(self):
        return self.driver.find_element(*FilterLocators.SORT_POPULARITY)

    @property
    def price_sort(self):
        return self.driver.find_element(*FilterLocators.SORT_PRICE)

    @property
    def all_restaurants_btn(self):
        return self.driver.find_element(*FilterLocators.ALL_RESTAURANT)

    @property
    def reset_button(self):
        return self.driver.find_element(*FilterLocators.RESET)

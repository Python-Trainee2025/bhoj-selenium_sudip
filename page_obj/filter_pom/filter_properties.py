from page_obj.filter_pom.filter_locators import FilterLocators

class FilterProperties:

    @property
    def first_button(self):
        return self.driver.find_element(*FilterLocators.FIRST_BUTTON)

    @property
    def popup_select(self):
        return self.driver.find_element(*FilterLocators.POPUP_SELECT)

    @property
    def sort_dropdown(self):
        return self.driver.find_element(*FilterLocators.SORT_DROPDOWN)

    @property
    def sort_option3(self):
        return self.driver.find_element(*FilterLocators.SORT_OPTION_3)

    @property
    def filter_dropdown(self):
        return self.driver.find_element(*FilterLocators.FILTER_DROPDOWN)

    @property
    def filter_option3(self):
        return self.driver.find_element(*FilterLocators.FILTER_OPTION_3)

from page_obj.view_menu.view_menu_locaters import ViewMenuLocators


class ViewMenuProperties(ViewMenuLocators):

    @property
    def select_restaurant(self):
        return self.driver.find_element(*ViewMenuLocators.RESTAURANT)

    @property
    def select_category(self):
        return self.driver.find_element(*ViewMenuLocators.MENU_CATEGORY)


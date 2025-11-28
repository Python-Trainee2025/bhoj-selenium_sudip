from selenium.webdriver.common.by import By

class FilterLocators:

    # First button after login
    FIRST_BUTTON = (By.XPATH, "//span/img[@alt='Get Food Delivered']")

    # Popup location selection (any image inside modal)
    POPUP_SELECT = (By.XPATH, "//div[contains(@class,'modal-body')]//img")

    # Stable dropdowns using label text instead of dynamic IDs
    SORT_DROPDOWN = (By.XPATH, "//label[contains(text(),'Sort')]/following-sibling::select")
    SORT_OPTION_3 = (By.XPATH, "//label[contains(text(),'Sort')]/following-sibling::select/option[3]")

    FILTER_DROPDOWN = (By.XPATH, "//label[contains(text(),'Filter')]/following-sibling::select")
    FILTER_OPTION_3 = (By.XPATH, "//label[contains(text(),'Filter')]/following-sibling::select/option[3]")

import logging
from selenium.webdriver.common.by import By


class SearchLocators(object):
    logging.info("SearchLocators loaded")

    SEARCH_BOX = (By.XPATH, "//input[@id='exampleInput1']")
    DROPDOWN = (By.XPATH, "//div[@class= 'main-auto-suggestion']//ul")
    DROPDOWN_ITEMS = (By.XPATH, "//div[@class='main-auto-suggestion']//span")
    RESTAURANT_OPTION = (
        By.XPATH,
        '//span[normalize-space()="The Burger House and Crunchy Fried Chicken (Kuleshwor)"]'
    )

    TODAY_DEAL = (By.XPATH, "//h2[normalize-space()=\"Today's Deals\"]")
    BROWSE_CATEGORY = (By.XPATH, "//label[@for='Bakery']")
    BROWSE_CUISINE = (By.XPATH, "//label[contains(text(),'Indian')]")
    SORT_POPULARITY = (By.XPATH, "//div[contains(@class,'pr-md-0')]//div/select")
    SORT_PRICE = (By.XPATH, "//div[contains(@class,'col-sm-6 col-md-6 col-xl-3')][2]/div/select")
    ALL_RESTAURANT = (By.XPATH, "//h2[normalize-space()='All Restaurants']")
    RESET = (By.XPATH, "//button[normalize-space()='Reset']")

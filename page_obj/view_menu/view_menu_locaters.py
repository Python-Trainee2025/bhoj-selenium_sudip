import logging
from selenium.webdriver.common.by import By


class ViewMenuLocators(object):
    logging.info("ViewMenuLocators loaded")

    RESTAURANT = (By.XPATH, "//a/div[contains(@class,'restaurant-type')]")
    MENU_CATEGORY = (By.XPATH, '//div[contains(@class,"category-tab")]//li//a[text()="Chicken Burger"]')

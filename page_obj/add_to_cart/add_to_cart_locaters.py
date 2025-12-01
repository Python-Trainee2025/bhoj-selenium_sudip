import logging
from selenium.webdriver.common.by import By

class AddToCartLocators(object):
    logging.info("Loading AddToCartLocators")

    MENU_ITEMS = (By.XPATH, "//div[@id='menu-list-div']//a")
    FIRST_ITEM = (By.XPATH, "(//div[@id='menu-list-div']//a)[1]")
    SECOND_ITEM = (By.XPATH, "(//div[@id='menu-list-div']//a)[2]")

    ADD_QUANTITY = (
        By.XPATH,
        "(//i[@class='icon-add' and not(ancestor::div[contains(@style,'display:none')])])[1]"
    )

    SUBTRACT_QUANTITY = (
        By.XPATH,
        "//div[@id='mycartorder']//i[contains(@class,'icon-remove')]"
    )

from selenium.webdriver.common.by import By


class AddToCartLocators(object):

    # All menu items inside the menu list
    MENU_ITEMS = (By.XPATH, "//div[@id='menu-list-div']//a")

    # First menu item (the ADD anchor)
    FIRST_ITEM = (By.XPATH, "(//div[@id='menu-list-div']//a)[1]")

    # Second menu item
    SECOND_ITEM = (By.XPATH, "(//div[@id='menu-list-div']//a)[2]")

    # + icon inside the cart — first visible one
    ADD_QUANTITY = (
        By.XPATH,
        "(//i[@class='icon-add' and not(ancestor::div[contains(@style,'display:none')])])[1]"
    )

    SUBTRACT_QUANTITY = (
        By.XPATH,
        "//div[@id='mycartorder']//i[contains(@class,'icon-remove')]"
    )



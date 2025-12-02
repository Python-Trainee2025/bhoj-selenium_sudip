from selenium.webdriver.common.by import By

class SearchStressLocators:
    SEARCH_BOX = (By.ID, "exampleInput1")
    SEARCH_SUGGESTIONS = (By.XPATH, "//div[contains(@class,'search-suggestion')]//a")

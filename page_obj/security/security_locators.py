from selenium.webdriver.common.by import By


class SecurityLocators:

    SEARCH_BOX = (By.ID, "exampleInput1")
    SEARCH_SUGGESTION_DROPDOWN = (By.CSS_SELECTOR, "ul.search-suggestion-list")
    NO_RESULTS_TEXT = (By.XPATH, "//p[contains(text(),'No results')]")

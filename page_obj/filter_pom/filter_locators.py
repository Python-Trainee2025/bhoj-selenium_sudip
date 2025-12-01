import logging
from page_obj.search.search_locators import SearchLocators


class FilterLocators:
    logging.info("FilterLocators loaded")

    TODAY_DEAL = SearchLocators.TODAY_DEAL
    BROWSE_CATEGORY = SearchLocators.BROWSE_CATEGORY
    BROWSE_CUISINE = SearchLocators.BROWSE_CUISINE
    SORT_POPULARITY = SearchLocators.SORT_POPULARITY
    SORT_PRICE = SearchLocators.SORT_PRICE
    ALL_RESTAURANT = SearchLocators.ALL_RESTAURANT
    RESET = SearchLocators.RESET

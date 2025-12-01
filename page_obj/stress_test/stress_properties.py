import logging


class StressProperties:

    logging.info("Loading Stress Test Keywords")
    RANDOM_KEYWORDS = [
        "burger", "pizza", "momo", "coffee", "cake", "fries",
        "thukpa", "sushi", "chowmin", "wrap"
    ]

    logging.info("Loading Stress Test Constants")
    TOTAL_REQUESTS = 50
    MIN_DELAY = 0.1
    MAX_DELAY = 0.4
    MAX_RESPONSE_TIME = 3

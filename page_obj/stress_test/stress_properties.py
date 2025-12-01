class StressProperties:

    RANDOM_KEYWORDS = [
        "burger", "pizza", "momo", "coffee", "cake", "fries",
        "thukpa", "sushi", "chaumin", "wrap"
    ]

    TOTAL_REQUESTS = 50            # number of rapid searches
    MIN_DELAY = 0.1                # seconds
    MAX_DELAY = 0.4

    MAX_RESPONSE_TIME = 3          # seconds allowed for search results

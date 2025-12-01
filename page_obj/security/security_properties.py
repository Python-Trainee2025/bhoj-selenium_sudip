import logging


class SecurityProperties:

    logging.info("Loading SQL payload list")
    SQL_PAYLOADS = [
        "' OR 1=1 --",
        "'; DROP TABLE users; --",
        "\" OR \"\" = \"",
        "' OR 'a'='a",
    ]

    logging.info("Loading XSS payload list")
    XSS_PAYLOADS = [
        "<script>alert('xss')</script>",
        "<img src=x onerror=alert(1)>",
        "<svg/onload=alert(1)>"
    ]

    logging.info("Setting RATE_LIMIT_COUNT to 25")
    RATE_LIMIT_COUNT = 25

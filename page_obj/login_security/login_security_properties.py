import logging


class LoginSecurityProperties:

    logging.info("Loading SQL injection payloads")
    SQL_PAYLOADS = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "'; DROP TABLE users; --",
        "' OR ''='",
        "\" OR \"\" = \"",
    ]


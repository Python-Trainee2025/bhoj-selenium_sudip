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

    logging.info("Loading brute-force password list")
    BRUTE_FORCE_PASSWORDS = [
        "wrong123",
        "password",
        "123456",
        "letmein",
        "wow111",
        "admin123",
        "invalid_pass",
        "wrongpassword1",
        "tryagain123",
    ]

    logging.info("Setting MAX brute force attempts")
    MAX_BRUTE_FORCE_ATTEMPTS = 10

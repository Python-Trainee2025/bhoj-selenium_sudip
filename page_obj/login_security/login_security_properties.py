class LoginSecurityProperties:

    SQL_PAYLOADS = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "'; DROP TABLE users; --",
        "' OR ''='",
        "\" OR \"\" = \"",
    ]

    BRUTE_FORCE_PASSWORDS = [
        "wrong123",
        "password",
        "123456",
        "letmein",
        "qwerty",
        "admin123",
        "invalid_pass",
        "wrongpassword1",
        "tryagain123",
    ]

    MAX_BRUTE_FORCE_ATTEMPTS = 10

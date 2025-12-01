class SecurityProperties:
    # SQL injection payloads
    SQL_PAYLOADS = [
        "' OR 1=1 --",
        "'; DROP TABLE users; --",
        "\" OR \"\" = \"",
        "' OR 'a'='a",
    ]

    # XSS payloads
    XSS_PAYLOADS = [
        "<script>alert('xss')</script>",
        "<img src=x onerror=alert(1)>",
        "<svg/onload=alert(1)>"
    ]

    # Number of searches in quick succession (for rate limiting)
    RATE_LIMIT_COUNT = 25

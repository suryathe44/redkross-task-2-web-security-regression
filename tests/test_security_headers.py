REQUIRED_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
}


def test_required_security_headers_on_health(client):
    response = client.get("/health")
    for name, expected in REQUIRED_HEADERS.items():
        assert response.headers.get(name) == expected


def test_content_security_policy_present(client):
    value = client.get("/health").headers.get("Content-Security-Policy", "")
    assert "default-src 'self'" in value
    assert "frame-ancestors 'none'" in value


def test_sensitive_responses_are_not_cached(client):
    assert client.get("/account").headers.get("Cache-Control") == "no-store"

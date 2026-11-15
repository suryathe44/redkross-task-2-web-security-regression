def test_account_requires_authentication(client):
    assert client.get("/account").status_code == 401


def test_regular_user_cannot_access_admin_area(client):
    assert client.post("/login/user").status_code == 200
    assert client.get("/admin").status_code == 403


def test_admin_can_access_admin_area(client):
    assert client.post("/login/admin").status_code == 200
    response = client.get("/admin")
    assert response.status_code == 200
    assert response.get_json()["admin"] is True


def test_logout_removes_authenticated_session(client):
    client.post("/login/user")
    assert client.post("/logout").status_code == 200
    assert client.get("/account").status_code == 401

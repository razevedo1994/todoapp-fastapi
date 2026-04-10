from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        "users",
        json={
            "username": "testuser",
            "password": "password",
            "email": "test@test.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "testuser",
        "email": "test@test.com",
    }


def test_read_users(client):
    response = client.get("users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {"id": 1, "username": "testuser", "email": "test@test.com"},
        ]
    }


def test_read_user(client):
    response = client.get("users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "testuser",
        "email": "test@test.com",
    }


def test_read_user_not_found(client):
    response = client.get("users/2")

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        "users/1",
        json={
            "username": "TESTUSER",
            "password": "password",
            "email": "test@test.com",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1, "username": "TESTUSER", "email": "test@test.com"
    }


def test_update_user_not_found(client):
    response = client.put(
        "users/2",
        json={
            "username": "TESTUSER",
            "password": "password",
            "email": "test@test.com",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND

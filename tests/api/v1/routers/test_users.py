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
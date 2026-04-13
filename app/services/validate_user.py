from http import HTTPStatus

from fastapi import HTTPException


def user_exist(user_id: int, database: list):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User with id not found."
        )

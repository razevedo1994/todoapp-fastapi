from http import HTTPStatus

from fastapi import HTTPException


def get_or_404(
    user_id: int, database: list, detail: str = "Resource not found."
):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=detail)

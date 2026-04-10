from http import HTTPStatus

from app.schemas import UserDB, UserList, UserPublic, UserSchema
from fastapi import APIRouter, HTTPException

user_database = []

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(user_database) + 1, **user.model_dump())

    user_database.append(user_with_id)

    return user_with_id


@router.get("/", status_code=HTTPStatus.OK, response_model=UserList)
async def read_users():
    return {"users": user_database}


@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=UserPublic)
async def read_user(user_id: int):
    if user_id < 1 or user_id > len(user_database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User with id not found."
        )

    user = user_database[user_id - 1]

    return user

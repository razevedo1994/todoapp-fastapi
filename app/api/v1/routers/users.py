from http import HTTPStatus

from app.core import get_or_404
from app.schemas import UserDB, UserList, UserPublic, UserSchema
from fastapi import APIRouter

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
    get_or_404(user_id, user_database)

    user = user_database[user_id - 1]

    return user


@router.put("/{user_id}", status_code=HTTPStatus.OK, response_model=UserPublic)
async def update_user(user_id: int, user: UserSchema):
    get_or_404(user_id, user_database)

    user_with_id = UserDB(id=user_id, **user.model_dump())

    user_database[user_id - 1] = user_with_id

    return user_with_id

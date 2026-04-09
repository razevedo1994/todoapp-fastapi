from http import HTTPStatus

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

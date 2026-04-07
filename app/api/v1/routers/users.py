from http import HTTPStatus

from fastapi import APIRouter

from schemas import UserDB, UserPublic, UserSchema

user_database = []

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(user_database) + 1, **user.model_dump())

    user_database.append(user_database)

    return user_with_id

from http import HTTPStatus

from app.core import get_or_404
from app.schemas import TaskSchema
from fastapi import APIRouter
from .users import user_database

tasks_database = []

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED)
async def create_task(user_id: int, task: TaskSchema):
    get_or_404(user_id, user_database)

    pass

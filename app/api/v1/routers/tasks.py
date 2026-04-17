from http import HTTPStatus

from app.core import get_or_404
from app.schemas import TaskDB, TaskPublic, TaskSchema
from fastapi import APIRouter

from .users import user_database

tasks_database = {}

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=TaskPublic)
async def create_task(user_id: int, task: TaskSchema):
    get_or_404(user_id, user_database)

    task_with_id = TaskDB(
        task_id=len(tasks_database.get(user_id)) + 1
        if tasks_database.get(user_id)
        else 1,  # TO-DO: Refactor creation of the task id
        **task.model_dump(),
    )

    tasks_database[user_id] = task_with_id

    return task_with_id

from http import HTTPStatus
from collections import defaultdict

from app.core import get_or_404
from app.schemas import TaskDB, TaskPublic, TaskSchema, TaskList
from fastapi import APIRouter

from .users import user_database

tasks_database = defaultdict(list)

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

    tasks_database[user_id].append(task_with_id)

    return task_with_id

@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=TaskList)
async def read_user_tasks(user_id: int):
    get_or_404(user_id, user_database)

    user_tasks = tasks_database[user_id]

    return {"tasks": user_tasks}

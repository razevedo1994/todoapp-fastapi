from enum import Enum

from pydantic import BaseModel


class Status(str, Enum):
    PENDING = "pending"
    DOING = "doing"
    COMPLETE = "completed"


class TaskSchema(BaseModel):
    task: str
    priority: str
    status: Status = Status.PENDING


class TaskDB(TaskSchema):
    task_id: int


class TaskPublic(BaseModel):
    task_id: int
    task: str
    priority: str
    status: Status

class TaskList(BaseModel):
    tasks: list[TaskPublic]

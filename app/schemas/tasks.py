from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    task: str
    status: str

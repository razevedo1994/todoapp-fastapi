from fastapi import FastAPI

from app.api.v1.routers import tasks, users

app = FastAPI()


app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Fast TODO-APP"}

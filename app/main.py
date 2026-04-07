from fastapi import FastAPI

from api.v1.routers import users

app = FastAPI()


app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Fast TODO-APP"}

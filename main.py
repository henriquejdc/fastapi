from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role
from uuid import UUID

app = FastAPI()


db: List[User] = [
    User(
        id=UUID("68bddf1a-a542-4842-a59d-8967922ad9a8"), 
        first_name="Henrique", 
        last_name="Corte", 
        gender=Gender.male,
        roles=[Role.admin, Role.student]
    ),
    User(
        id=UUID("49e33899-5cb7-4eb5-8a2a-3801007319d0"), 
        first_name="Tais", 
        last_name="Oliveira", 
        gender=Gender.female,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    # await foo()
    return {"Api": "Users"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.get("/api/v1/user/{user_id}")
async def fetch_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )


@app.post("/api/v1/user")
async def register_user(user: User):
    db.append(user)
    return {"New user id": user.id}


@app.put("/api/v1/user")
async def update_user(user_update: User):
    for user in db:
        if user.id == user_update.id:
            if user_update.first_name:
                user.first_name = update_user.first_name
            if user_update.middle_name:
                user.middle_name = update_user.middle_name
            if user_update.last_name:
                user.last_name = update_user.last_name
            if user_update.gender:
                user.gender = update_user.gender
            if user_update.roles:
                user.roles = update_user.roles
            return "Updated User"

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )


@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return "Deleted User!"

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )
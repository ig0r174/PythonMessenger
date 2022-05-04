from fastapi import APIRouter

from schemas.user import User, UserInDB
from crud.user import user_database

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/{user_id}")
def get_user(user_id: int):
    return user_database[user_id - 1]


@router.post("/", response_model=UserInDB)
def create_user(user: User):
    # Добавляем пользователя в бд
    user_db = UserInDB(id=len(user_database) + 1, **user.dict())
    return user_db


@router.put("/", response_model=UserInDB)
def update_user(user_id: int, user: User):
    # Обновить пользователя
    user_db = user_database[user_id - 1]
    for param, value in user.dict():
        user_db[param] = value
        # здесь изменения сохраняются в базу

    return user_db


@router.delete("/{user_id}")
async def update_user(user_id: int):
    db = list(user_database)
    del db[user_id - 1]

    return db

from fastapi import APIRouter, Depends, HTTPException, status

from schemas.user import User, UserInDB
import crud.user as crud
from deps import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/{user_id}")
def get_user(user_id: int, db=Depends(get_db())):
    user = crud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


@router.post("/", response_model=UserInDB)
def create_user(user: User, db=Depends(get_db())):
    result = crud.create_user(db=db, user=user)
    return result


@router.put("/", response_model=UserInDB)
def update_user(user_id: int, user: User, db=Depends(get_db())):
    user_db = crud.update_user(db=db, user_id=user_id, user=user)
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user_db


@router.delete("/{user_id}")
async def update_user(user_id: int, db=Depends(get_db())):
    crud.delete_user(db=db, user_id=user_id)

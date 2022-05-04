from fastapi import APIRouter

from crud.user import user_database
from crud.chat import chat_database, user_chat_database
from schemas.chat import Chat, ChatInDB



router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.get('/{chat_id}')
def get_chat(chat_id: int):
    chat = chat_database[chat_id-1]
    new_user_db = []
    for ref in user_chat_database:
        if ref['chat_id'] == chat_id:
            for user in user_database:
                if user['id'] == ref['user_id']:
                    new_user_db.append(user)

    return chat, new_user_db


@router.post("/", response_model=ChatInDB)
def create_chat(chat: Chat):
    chat_db = ChatInDB(id=len(chat_database)+1, **chat.dict())
    return chat_db


@router.put("/", response_model=ChatInDB)
def update_chat(chat_id: int, chat: Chat):
    chat_db = chat_database[chat_id-1]
    for param, value in chat.dict():
        chat_db[param] = value

    return chat_db

@router.delete('/{chat_id}')
async def update_chat(chat_id: int):
    db = list(chat_database)
    del db[chat_id-1]

    return db


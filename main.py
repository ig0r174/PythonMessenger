from fastapi import FastAPI
import uvicorn

from endpoints.user import router as user_router
from endpoints.chat import router as chat_router

app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8080,
        reload=True,
        debug=True,
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}

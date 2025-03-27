from fastapi import FastAPI, Form, HTTPException, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Пример базы данных пользователей
users_db = {
    "user123": "password123"
}

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username in users_db and users_db[username] == password:
        # Генерация уникального токена
        session_token = "abc123xyz456"
        
        # Установка файла cookie
        response = JSONResponse(content={"message": "Logged in successfully"})
        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,
            secure=True,
            samesite="strict"
        )
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
from fastapi import Cookie

@app.get("/user")
async def get_user(session_token: str | None = Cookie(default=None)):
    if session_token == "abc123xyz456":  # Проверка токена
        return {"username": "user123", "email": "user@example.com"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

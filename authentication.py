from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from fastapi import HTTPException
from fastapi import APIRouter

#part not used about authentication

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "123",  # Em produção, use senhas criptografadas
        "token": "secrettoken"
    }
}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": user["token"], "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    for user in fake_users_db.values():
        if token == user["token"]:
            return user
    raise HTTPException(status_code=401, detail="Invalid or expired token")

@router.get("/secure-data/")
def read_secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['username']}! You are authorized."}



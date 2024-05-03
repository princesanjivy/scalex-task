from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from model.user import User
from data import user as db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: add this to .env or export it as these are constants
SECRET_KEY = "scalex-assignment"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate token"
    )
    user_id = 0
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        # print(e)
        raise credentials_exception
    user = db.get_user(id=int(user_id)) # keeping id as int, since token contains user_id as str
    if not user: # add validation for user not found
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"user not found"}
        )
    return user

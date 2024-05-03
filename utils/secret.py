from datetime import datetime, timedelta
from jose import jwt

# TODO: add this to .env or export it as these are constants
SECRET_KEY = "scalex-assignment"
ALGORITHM = "HS256"

# to generate a JWT token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expires = datetime.now() + expires_delta
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

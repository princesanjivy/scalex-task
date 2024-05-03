# this router contains endpoints for getting the JWT token
# /login => used to generate the auth token for admins to login

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from model.user import Token, Payload
from utils import secret
from data import user as db
from datetime import timedelta

router = APIRouter(
    prefix="/auth"
)

@router.post("/login", response_model=Token)
def login(data: Payload):
    user = db.get_user(id=data.user_id)
    if not user: # add validation for user not found
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"user not found"}
        )
    expires_delta = timedelta(minutes=15)
    # sub part can only contain string as the type hence, implictiy converting id to string
    token_data = {"sub":str(user.id), "username":user.name}
    # generate the access token
    access_token = secret.create_access_token(
        data=token_data, 
        expires_delta=expires_delta
    )
    response = Token(type="bearer", access_token=access_token)
    return response

# this router contians all the CRUD endpoints on library's book
# /home => lists out all the books there in the database (regularUser.csv)
# /addBook => used to add a new book entry to the database (regularUser.csv)
# /deleteBook => used to delete a book entry from the database (regularUser.csv)

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from typing import List
from model.book import Book, RemoveBookReq
from model.user import User
from utils import user as util
from data import book as db

router = APIRouter(
    prefix="/book"
)

@router.get("/home", response_model=List[Book])
def home(current_user: User = Depends(util.get_current_user)):
    rb = db.get_regular_books()
    if current_user.is_admin:
        # give all the books in the database
        books = []
        ab = db.get_admin_books()
        books.extend(ab)
        books.extend(rb)
        return books
    else:
        return rb

@router.post("/addBook")
def add_book(payload: Book, current_user: User = Depends(util.get_current_user)):
    if not current_user.is_admin:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":f"user {current_user.name.lower()} doesn't have access to add book"}
        )
    # add book to the db (regularUser.csv)
    db.add_book(payload)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="")

@router.delete("/removeBook")
def add_book(payload: RemoveBookReq, current_user: User = Depends(util.get_current_user)):
    if not current_user.is_admin:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":f"user {current_user.name.lower()} doesn't have access to remove book"}
        )
    if db.remove_book(payload.book_name) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":f"{payload.book_name}"}) 
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message":f"{payload.book_name} book has been deleted"})

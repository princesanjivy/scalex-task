from pydantic import BaseModel, Field

class Book(BaseModel):
    book_name: str = Field(alias="Book Name")
    author: str = Field(alias="Author")
    publication_year: int = Field(alias="Publication Year")

class RemoveBookReq(BaseModel):
    book_name: str = Field(alias="Book Name")
    
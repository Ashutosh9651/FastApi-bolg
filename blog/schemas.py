from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title:str
    body:str



class User(BaseModel):
    email:str
    password:str
    name:str

class ShowUser(BaseModel):
    email:str
    name:str

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
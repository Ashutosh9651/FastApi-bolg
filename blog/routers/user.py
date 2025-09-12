from fastapi import APIRouter, FastAPI,Depends,status,Response,HTTPException
from typing import List
from ..database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .. import schemas, models,hashing
from ..repository import user



router = APIRouter(
    prefix = "/user",
    tags=['Users']
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db: Session = Depends(get_db)):
    return user.create_user(request,db)



@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)
   
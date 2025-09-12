from fastapi import APIRouter, FastAPI,Depends,status,Response,HTTPException
from typing import List
from ..database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .. import schemas, models,hashing,Oauth2
from ..repository import blog


router = APIRouter(
    prefix = '/blog',
    tags=['Blogs']
)


@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.get_all(db)
 

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.create(request,db)
 

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.update(id,request,db)

    
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.destroy(id,db)
   

@router.get('/{id}', response_model=schemas.ShowBlog)
def show(id:int,  db : Session = Depends(get_db),current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.show(id,db)
   
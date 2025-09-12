from fastapi import APIRouter, FastAPI,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models,hashing
from ..database import engine, SessionLocal



def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    db.delete(blog)
    db.commit()

    return {"message": "Blog deleted successfully"}

def update(id:int,request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    existing_blog = blog.first()
    if not existing_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog.update(request.dict(), synchronize_session=False)
    db.commit()

    return {"message": "Blog updated successfully"}

def show(id:int,db : Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Blog not found for id = {id}")
            
    return blogs
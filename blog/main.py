from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog,user,authenticate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authenticate.router)


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     existing_blog = blog.first()
#     if not existing_blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with id {id} not found"
#         )

#     blog.update(request.dict(), synchronize_session=False)
#     db.commit()

#     return {"message": "Blog updated successfully"}

# @app.delete('/blog/{id}', status_code=status.HTTP_200_OK,tags=['blogs'])
# def destroy(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()

#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with id {id} not found"
#         )

#     db.delete(blog)
#     db.commit()

#     return {"message": "Blog deleted successfully"}


# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', response_model=schemas.ShowBlog,tags=['blogs'])
# def show(id,  db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()

#     if not blogs:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#         detail = f"Blog not found for id = {id}")
        
#     return blogs



# @app.post('/user',response_model=schemas.ShowUser,tags=['users'])
# def create_user(request:schemas.User,db: Session = Depends(get_db)):

#     new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
# def get_user(id,db:Session=Depends(get_db)):
#     users = db.query(models.User).filter(models.User.id==id).first()
#     if not users:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User not found")
#     return users
    


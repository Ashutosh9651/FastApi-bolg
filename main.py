from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

app = FastAPI()

# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9898)


@app.get('/blog')
def index(limit = 10,published:bool = True, sort:Optional[str] = None):

    if published:

        return {'data':f'{limit} blogs comes in db'}
    else:
        return {'data':'all the blogs'}


@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all unpublished blog"}



@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


#=============================================================================================
# POST Data
#=============================================================================================

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"blog is created with {blog.title}"}
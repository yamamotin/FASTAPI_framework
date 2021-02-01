from fastapi import FastAPI
import uvicorn
import databases
import sqlalchemy
from typing import List

from crud.schema import Cats

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

# Methodos de manipulação do bd

@app.get("/get", response_model=List[Cats], status_code=200)
async def get_cats():
    query = Cats.select()
    cats = await database.fetch_all(query)
    if cats is None:
        return {"message": " Nenhum cat existente!"}
    else:
        return cats


@app.get("/get/{id}", response_model=Cats, status_code=200)
async def get_cat_by_id(id:int):
    query = Cats.select().where(Cats.id == id)
    return await database.fetch_one(query=query)


@app.post("/create/", response_model=Cats, status_code=201)
async def create_cat(cat: Cats):
    query = cats.insert().values(breed=post.breed, loc_origing=post.loc_origin, coat_lenght=post.coat_lenght,
                                  pattern=post.pattern)
    createquery = await database.execute(query=query)
    return {**query.dict(), "id": createquery}


@app.put("/update/{id}", response_model=Cats)
async def update(id:int, post: Cats):
    query = Cats.update().where(Cats.id == id).values(breed=post.breed, loc_origing=post.loc_origin, coat_lenght=post.coat_lenght, patter=post.pattern,)
    updateid = await database.execute(query=query)
    return {**post.dict(), "id": updateid}


@app.delete("/delete/{id}", response_model=Post)
async def delete(id:int):
    query = posts.delete().where(posts.c.id == id)
    return await database.execute(query)

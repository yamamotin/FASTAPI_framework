from fastapi import FastAPI
import sqlalchemy
import uvicorn

from typing import List
from crud.model import cats, database
from crud.schema import Cats

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#DB connection
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Methodos de manipulação do bd
@app.get("/get", response_model=List[Cats])
async def get_cats():
    query = cats.select(cats.c.id != None)
    allcats = await database.fetch_all(query)
    return allcats


@app.get("/get/{buscador}", response_model=Cats, status_code=200)
async def get_cat_by_id(buscador):
    query = cats.select().where(cats.c.buscador == buscador)
    catid = await database.fetch_one(query=query)
    return catid
    

@app.post("/create/", response_model=Cats, status_code=201)
async def create_cat(post: Cats):
    query = cats.insert().values(breed=post.breed, loc_origing=post.loc_origin, coat_lenght=post.coat_lenght,pattern=post.pattern)
    createdquery = await metadata.query
    return {**post.dict(), "id": createdquery}


@app.put("/update/{id}", response_model=Cats)
async def update(id:int, post: Cats):
    query = Cats.update().where(Cats.id == id).values(breed=post.breed, loc_origing=post.loc_origin, coat_lenght=post.coat_lenght, patter=post.pattern,)
    updateid = await database.execute(query=query)
    return {**post.dict(), "id": updateid}


@app.delete("/delete/{id}", response_model=Cats)
async def delete(id:int):
    query = posts.delete().where(posts.c.id == id)
    return await database.execute(query)

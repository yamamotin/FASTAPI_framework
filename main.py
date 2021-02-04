from fastapi import FastAPI
import uvicorn, uuid, sqlalchemy

from typing import List
from crud import model
from crud.model import cats, database, metadata, engine
from crud.schema import Cats, CatsRegister

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#DB connection
@app.on_event("startup")
async def startup():
    metadata.create_all(engine)
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

#TODO
@app.get("/get/{buscador}/{comparador}", response_model=List[Cats])
async def get_cat_by_id(buscador, comparador):
    query = await get_cats()
    onlycats = []
    for cat in query:
        if cat[buscador] == comparador:
            onlycats.append(cat)
    return onlycats

@app.post("/create/", response_model=Cats, status_code=201)
async def create_cat(cat: CatsRegister):
    gID = int(uuid.uuid1())
    query = cats.insert().values(
        breed=cat.breed,
        location_of_origin=cat.location_of_origin, 
        coat_length=cat.coat_length,
        body_type=cat.body_type,
        pattern=cat.pattern
    )
    
    await database.execute(query)
    return {
        "id":gID,
        **cat.dict(),
    }


@app.put("/update/{id}", response_model=Cats)
async def update(id:int, post: CatsRegister):
    query = cats.update().where(cats.c.id == id).values(
        breed=post.breed, 
        location_of_origin=post.location_of_origin,
        coat_length=post.coat_length,
        body_type=post.body_type,
        pattern=post.pattern
        )
    await database.execute(query=query)
    return {**post.dict(), "id":id}

@app.delete("/delete/{id}", response_model=Cats)
async def delete(id: int):
    query = cats.delete().where(cats.c.id == id)
    await database.execute(query)
    return True
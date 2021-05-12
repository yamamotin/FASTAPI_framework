from fastapi import FastAPI
from fastapi.routing import APIRouter
from sqlalchemy.sql.expression import false
from starlette.responses import RedirectResponse
import uvicorn, uuid, sqlalchemy

from typing import List
from crud import model
from crud.model import cats, database, metadata, engine
from crud.schema import Cats, CatsRegister

app = FastAPI()
crudroute = APIRouter()
app.include_router(crudroute,prefix="/crud")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

#DB connection
@app.on_event("startup")
async def startup():
    metadata.create_all(engine)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Methodos de manipulação do bd
@app.get("/")
async def redirect():
    adminpage = RedirectResponse(url='http://127.0.0.1:8000/docs#/')
    return adminpage

@app.get("/get", response_model=List[Cats])
async def get_cats():
    query = cats.select(cats.c.id != None)
    allcats = await database.fetch_all(query)
    return allcats

#TODO
@app.get("/get/{parametro}/{comparador}", response_model=List[Cats])
async def get_cat_by_id(parametro, comparador):
    allcats = await get_cats()
    onlycats = []
    for cat in allcats:
        if parametro.lower() == "pattern":
            if comparador.lower() == "false" and cat.pattern == 0:
                onlycats.append(cat)
            elif comparador.lower() == "true" and cat.pattern == 1:
                onlycats.append(cat)
        elif cat[parametro].lower() == comparador.lower():
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
    await database.execute(cats.delete().where(cats.c.id == id))
    return []

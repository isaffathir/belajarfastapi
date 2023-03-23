from typing import Union
from fastapi import FastAPI, Body
import schemas

app = FastAPI()

fake_db = {
    1:{
    'name': 'burger'
    },
    2:{
    'name': 'pizza'
    },
    3:{
    'name': 'pasta'
    },
}

@app.get("/")
async def read_root():
    return {" Hello World "}

@app.get("/foods")
async def getFoods():
    return fake_db

@app.get("/foods/{id}")
async def getFoods(id: int):
    return fake_db[id]

@app.post("/foods")
async def addFoods(food: schemas.Food):
    newId = len(fake_db) + 1
    
    fake_db[newId] = {'name': food.name}
    return fake_db

@app.put("/foods/{id}")
async def updateFoods(id: int, food: schemas.Food):
    fake_db[id]['name'] = food.name
    return fake_db

@app.delete("/foods/{id}")
async def deleteFoods(id: int):
    del fake_db[id]
    return fake_db

from fastapi import FastAPI
from pydantic import BaseModel
from database import Database

app = FastAPI()
app.db = Database()   

class Champion(BaseModel):
    name: str
    region: str

@app.get('/')
def main():
    return {'champion': 'region'}

@app.get('/champions')
def get_champions():
    return app.db.all()

@app.get('/champions/{champion_name}')
def get_champion(champion_name: str):
    region = app.db.get(champion_name)
    return {champion_name: region}

@app.post('/champions')
def create_champion(champion: Champion):
    app.db.put(champion.name, champion.model_dump())
    return app.db.get(champion.name)

@app.delete('/champions/{champion_name}')
def delete_champion(champion_name: str):
    app.db.delete(champion_name)
    return {}
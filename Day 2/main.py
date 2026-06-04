#This program teaches about parameters.
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the home page"

@app.get("/station")
def station(station_num : int):
    if station_num == 1:
        return "Romani"
    elif station_num == 2:
        return "Kolarru"
    else:
        return "Error no such station"


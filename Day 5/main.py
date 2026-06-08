from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()

drones = []

class Device_Info(BaseModel):
    id : int
    model : int
    battery : str


@app.get("/")
def home():
    return "Welcome to the home page"

@app.post("/drones")
def create_drone(drone_info : Device_Info):
    drones.append(drone_info)
    return {"status": "success",
    "data": drone_info
    }

@app.get("/drones/{drone_id}")
def get_drone(drone_id:int):
    for drone in drones:
        if drone.id== drone_id:
            return {"drone_info": drone}
    return "Fail"

@app.put("/drone/{drone_id}")
def update_battery(drone_id:int):
    for drone in drones:
        if drone.id == drone_id:
            drone.battery = ""
            return drone
    return "failure"

@app.delete("/drone/{drone_id}")
def delete_drone(drone_id:int):
    for drone in drones:
        if drone.id == drone_id:
            drones.remove(drone)
            return drones
    return "failure"


from fastapi import FastAPI, Depends
from database import SessionLocal, engine, Base
from pydantic import BaseModel, Field
from typing import Optional
from models import Drone
from schemas import Device_Info
from sqlalchemy.orm import Session
from sqlalchemy import select

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return "Welcome to the home page"

@app.post("/drones")
def create_drone(drone_info : Device_Info, db: Session = Depends(get_db)):
    drone = Drone(
        id = drone_info.id,
        model = drone_info.model,
        battery = drone_info.battery
    )
    db.add(drone)
    db.commit()
    db.refresh(drone)
    return drone


@app.get("/drones/{drone_id}")
def get_drone(drone_id:int,db:Session=Depends(get_db)):
    drone = db.execute(select(Drone).where(Drone.id == drone_id)).scalar_one_or_none()
    if not drone:
        return "failure"
    return drone

@app.put("/drone/{drone_id}")
def update_battery(drone_id:int,db:Session=Depends(get_db)):
    drone = db.execute(select(Drone).where(Drone.id == drone_id)).scalar_one_or_none()
    if not drone:
        return "failure"
    else:
        drone.battery = ""
        db.commit()
        db.refresh(drone)
        return drone

@app.delete("/drone/{drone_id}")
def delete_drone(drone_id:int,db:Session=Depends(get_db)):
    drone = db.execute(select(Drone).where(Drone.id == drone_id)).scalar_one_or_none()
    if not drone:
        return "failure"
    else:
        db.delete(drone)
        db.commit()
        return "success"


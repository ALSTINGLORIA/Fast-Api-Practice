from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the home page"
class Device_Status(BaseModel):
    version:int
    mini_v: Optional[str]= None

class Device(BaseModel):
    name:str
    model:int
    status: Device_Status


@app.post("/list")
def list(input_val: Device):
    return "True"



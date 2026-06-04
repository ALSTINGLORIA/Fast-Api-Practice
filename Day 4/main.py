from fastapi import FastAPI
from pydantic import BaseModel, Field
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
    model:int = Field(ge=1)
    status: Device_Status

class Response(BaseModel):
    model:int
    status: Device_Status


@app.post("/list", response_model=Response)
def list(input_val: Device):
    return input_val



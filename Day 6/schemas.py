from pydantic import BaseModel

class Device_Info(BaseModel):
    id : int
    model : int
    battery : str

    class Config:
        from_attributes = True

        

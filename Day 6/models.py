from sqlalchemy import Column, Integer, String
from database import Base

class Drone(Base):
    __tablename__ = "drones"
    id = Column(Integer, primary_key = True, index = True)
    model = Column(Integer)
    battery = Column(String)
    

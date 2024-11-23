from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    
    id = Column(Integer, primary_key=True)
    device_id = Column(String, unique=True)
    device_no = Column(Integer)
    name = Column(String)
    model = Column(String, nullable=True)
    status = Column(String)
    last_seen = Column(DateTime, default=datetime.utcnow)
    is_online = Column(Boolean, default=False)
    is_otg = Column(Boolean, default=False)
    is_cloud = Column(Boolean, default=False)
    current_action = Column(String, nullable=True, default="")
    buffer = Column(String, nullable=True, default="")

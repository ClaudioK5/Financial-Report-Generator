from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from database import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)

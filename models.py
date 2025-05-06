from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Graphs(Base):
    __tablename__ = 'Graphs'
    id = Column(Integer, primary_key=True, index=True)
    nodes = Column(String, index=True)
    adjency_list = Column(String, index=True)

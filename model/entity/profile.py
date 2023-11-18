import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column

from model.entity.base import Base

class Profile(Base):
    __tablename__ = "profile_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))


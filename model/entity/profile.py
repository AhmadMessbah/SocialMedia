from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.da.database import DataBaseManager
from model.entity.base import Base


class Profile(Base):
    __tablename__ = "profile_tbl"

    profileid = Column(Integer, primary_key=True, autoincrement=True, default=None)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))

    def __init__(self, name, family, username, password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password


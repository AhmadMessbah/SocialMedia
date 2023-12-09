from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.entity import *

class Profile(Base):
    __tablename__ = "profile_tbl"

    id = Column(Integer, primary_key=True)
    _name = Column("name",String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))

    posts = relationship("Post", back_populates="profile")

    def __init__(self, name, family, username, password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    @property
    def name(self):
        print("GETTER")
        return self._name

    @name.setter
    def name(self, name):
        print("SETTER")
        self._name = name


# model/entity/profile.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity.base import Base


class Profile(Base):
    __tablename__ = "profile_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))


    posts = relationship("Post", back_populates="profile")

    def __init__(self, name, family, username, password):
        super().__init__()
        self.name = name
        self.family = family
        self.username = username
        self.password = password


#a = Profile('behnam', 'masoumi', 'behnamlive', 'behnam126')
#print(a)
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from model.entity.base import Base
from model.entity import *

class Comment(Base):
    __tablename__ = "comment_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    text = Column(String(300))
    date_time = Column(DateTime)

    #post = relationship("Post")
   # profile = relationship("Profile")


    def __init__(self,  text):
        self.text = text
        # self.date_time = date_time
    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

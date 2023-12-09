from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey

from model.da.database import DataBaseManager
from model.entity.base import Base
from model.entity import *

class Comment(Base):
    __tablename__ = "comment_tbl"

    commentid = Column(Integer, primary_key=True, autoincrement=True, default=None)
    profileid = Column(Integer, ForeignKey('profile_tbl.profileid', ondelete='CASCADE'), nullable=False)
    post_idd = Column(Integer, ForeignKey("post_tbl.postid"))
    text = Column(String(300))
    #date_time = Column(DateTime)

    def __init__(self, profileid , post_idd, text):
        self. profileid =  profileid
        self.post_idd = post_idd
        self.text = text

a = Comment(1,1,'salam khubi')
b =  DataBaseManager()
b.save(a)





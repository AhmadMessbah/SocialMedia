from sqlalchemy import Column, Integer,DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from model.entity.base import *

class Like(Base):
    __tablename__ = "like_tbl"

    id = Column(Integer, primary_key=True,autoincrement=True,default=None)
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    date_time = Column(DateTime)

    profile = relationship("Profile")
    post = relationship("Post", back_populates="likes")

    def __init__(self, profile,post):
        self.profile = profile
        self.post = post
        self.date_time = datetime.now()


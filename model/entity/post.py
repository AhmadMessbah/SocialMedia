# model/entity/post.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from model.entity.base import Base

class Post(Base):
    __tablename__ = "post_tbl"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    text = Column(String(300))
    image = Column(String(300))
    date_time = Column(DateTime, default=datetime.now())

    likes = relationship("model.entity.like.Like", backref="post")
    profile = relationship("model.entity.profile.Profile", back_populates="posts")

    def __init__(self, text, image=None):
        self.text = text
        self.image = image
        #self.date_time = datetime.now()
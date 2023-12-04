from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from model.entity import *

class Post(Base):
    __tablename__ = "post_tbl"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    text = Column(String(300))
    image = Column(String(300))
    date_time = Column(DateTime)

    profile = relationship("Profile", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    comments = relationship("Comment", back_populates="post")

    def __init__(self, text, image=None):
        self.text = text
        self.image = image
        self.date_time = datetime.now()


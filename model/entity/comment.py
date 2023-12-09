from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from datetime import datetime

from model.entity import *


class Comment(Base):
    __tablename__ = "comment_tbl"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile_tbl.id'))
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    text = Column(String(300))
    date_time = Column(DateTime)

    profile = relationship("Profile")
    post = relationship("Post", back_populates="comments")

    def __init__(self, profile, post, text):
        self.profile = profile
        self.post = post
        self.text = text
        self.date_time = datetime.now()

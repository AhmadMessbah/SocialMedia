import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column, DateTime
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Comment(Base):
    __tablename__ = "comment_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    profile_id = Column(Integer, ForeignKey("post.id"))
    text = Column(String(250))
    date_time = Column(DateTime)

    post = relationship("Post")
    profile = relationship("profile")


    def __init__(self, code, post, profile, text, date_time):
        self.code = code
        self.post = post
        self.profile = profile
        self.text = text
        self.date_time = date_time

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Like(Base):
    __tablename__ = "like_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    profile_id = Column(Integer, ForeignKey("profile.id"))

    post = relationship("Post")
    profile = relationship("Profile")

    def __init__(self, post, profile):
        self.post = post
        self.profile = profile

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())


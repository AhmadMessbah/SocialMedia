import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Like(Base):
    __tablename__ = "like_tbl"
    # id = Column(Integer, primary_key=True)
    # post_id = Column(Integer, ForeignKey("post_tbl.id"))
    # profile_id = Column(Integer, ForeignKey("profile_tbl.id"))

    # post = relationship("Post",back_populates="likes")
    # profile = relationship("Profile")


    # def __init__(self, id, post, profile):
    #     self.id = id
    #     self.post = post
        # self.profile = profile

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

    @property
    def code(self):
        return self._id

    @code.setter
    def id(self, id):
        Validator.is_number(id, True, "Invalid Code")
        self.id = id

    @property
    def post(self):
        return self.post

    @post.setter
    def post(self, post):
        if isinstance(post, str) and re.match("^[a-zA-Z\s]{2,30}$", post):
            self.post = post
        else:
            raise ValueError("invalid post")

    @property
    def profile(self):
        return self.profile

    @profile.setter
    def profile(self, profile):
        if isinstance(profile, str) and re.match("^[a-zA-Z\s]{2,30}$", profile):
            self._password = profile
        else:
            raise ValueError("invalid profile")

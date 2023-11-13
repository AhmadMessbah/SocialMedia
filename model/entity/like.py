import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Profile(Base):
    __tablename__ = "like_tbl"

    def __init__(self, code, post, profile):
        self.code = code
        self.post = post
        self.profile = profile

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        Validator.is_number(code, True, "Invalid Code")
        self._code = code

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

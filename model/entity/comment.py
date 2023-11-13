import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Comment(Base):
    __tablename__ = "comment_tbl"

    def __init__(self, id, post, profile, text, date_time):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

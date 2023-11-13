import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Post(Base):
    __tablename__ = "post_tbl"

    def __init__(self, id, profile, text, image, date_time):
        self.id = id
        self.profile = profile
        self.text = text
        self.image = image
        self.date_time = date_time

    def __repr__(self):
        return str(self.__dict__)

    def convert_to_tuple(self):
        return self.id, self.name, self.family

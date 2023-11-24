import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from model.entity.base import Base
from tools.validator import Validator


class Post(Base):
    __tablename__ = "post_tbl"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    text = Column(String(300))
    image = Column(String(300))
    date_time = Column(DateTime)
    profile = relationship("Profile",lazy="joined")

    def __init__(self, profile, text, image):
        self.profile = profile
        self.text = text
        self.image = image
        self.date_time = self.date_time.now()

    def __repr__(self):
        return str(self.__dict__)

    def convert_to_tuple(self):
        return self.id, self.name, self.family

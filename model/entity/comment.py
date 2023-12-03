from sqlalchemy.orm import relationship

from model.entity.base import Base
from sqlalchemy import Integer, String, Column, Date, DateTime, ForeignKey
from datetime import datetime

class Comment(Base):
    __tablename__ = "comment_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    text = Column(String(300))
    date_time = Column(DateTime)

    post = relationship("Post")
    profile = relationship("Profile")


    def __init__(self,  text):
        self.text = text
        self.date_time = datetime.now()

        def __init__(self, id, post, profile):
            self.id = id
            self.post = post
            # self.profile = profile




    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())
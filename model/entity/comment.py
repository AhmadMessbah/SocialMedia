from sqlalchemy.orm import relationship

from model.entity.base import Base
from sqlalchemy import Integer, String, Column, Date, DateTime, ForeignKey


class Comment(Base):
    __tablename__ = "comment_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))
    text = Column(String(300))
    date_time = Column(DateTime)

    post = relationship("Post")
    profile = relationship("Profile")


    # def __init__(self, code,post, profile, text, date_time):
    #     self.code = code
    #     self.post = post
    #     self.profile = profile
    #     self.text = text
    #     self.date_time = date_time

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())
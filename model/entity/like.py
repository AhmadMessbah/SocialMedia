from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, Date, DateTime, ForeignKey

from model.entity import *

class Like(Base):
    __tablename__ = "like_tbl"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))

    post = relationship("Post",back_populates="likes")
    profile = relationship("Profile")


    # def __init__(self, id, post, profile):
    #     self.id = id
    #     self.post = post
        # self.profile = profile


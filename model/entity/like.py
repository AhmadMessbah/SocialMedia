# model/entity/like.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.post import Post
from model.entity.profile import Profile

class Like(Base):
    __tablename__ = "like_tbl"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post_tbl.id"))
    profile_id = Column(Integer, ForeignKey("profile_tbl.id"))

    #post = relationship('model.entity.post.Post', backref="likes")
    profile = relationship(Profile)

    def __init__(self, post, profile):
        self.post = post
        self.profile = profile
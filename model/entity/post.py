from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.da.database import DataBaseManager
from model.entity.base import Base
from model.entity.profile import Profile

class Post(Base):
    __tablename__ = "post_tbl"

    postid = Column(Integer, primary_key=True, autoincrement=True, default=None)
    profileid = Column(Integer, ForeignKey('profile_tbl.profileid', ondelete='CASCADE'), nullable=False)
    text = Column(String(300))
    image = Column(String(300))

    def __init__(self, profileid, text, image=None):
        self.profileid = profileid
        self.text = text
        self.image = image


#Profile.posts = relationship("Post", back_populates="profile")
#Post.profile = relationship("Profile", back_populates="posts")


a = Post(1, 'behnam')


b = DataBaseManager()


b.save(a)
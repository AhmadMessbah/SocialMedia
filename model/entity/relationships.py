from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.post import Post
from model.entity.profile import Profile

Profile.posts = relationship(Post, back_populates="profile")
Post.profile = relationship(Profile, back_populates="posts")
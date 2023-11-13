from model.da.database import DatabaseManager
from model.entity import post
from model.entity.post import Post
from sqlalchemy import text, and_, or_

class PostDa(DatabaseManager):
    def find_by_profile_id(self, profile_id):
        self.make_engine()
        result = self.session.query(Post).filter(Post.profile.id == profile_id)
        self.session.close()
        return result
    def find_by_time(self, datetime1, datetime2):
        self.make_engine()
        result = self.session.query(Post).filter(and_(Post.date_time >= datetime1, Post.date_time <= datetime2 ))
        self.session.close()
        return result

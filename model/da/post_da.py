from model.da.database import *
from model.entity import *

class PostDa(DataBaseManager):
    def find_by_profile_id(self, profile_id):
        self.make_engine()
        result = self.session.query(Post).filter(Post.profile_id == profile_id)
        self.session.close()
        return result

    def find_by_profile_username(self, profile_username):
        self.make_engine()
        result = self.session.query(Post).filter(Post.profile.username == profile_username)
        self.session.close()
        return result

    def find_by_time(self, start_time, end_time):
        self.make_engine()
        result = self.session.query(Post).filter(between(Post.date_time >= start_time, Post.date_time <= end_time ))
        self.session.close()
        return result

    # todo : find_posts_count_by_profile_id

    
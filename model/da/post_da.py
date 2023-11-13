from model.da.database import DatabaseManager
from model.entity import post
from model.entity.post import Post


class PostDa(DatabaseManager):
    def find_by_profile_id(self, profile_id):
        self.make_engine()
        result = self.session.query(Post).filter(Post.profile.id == profile_id)
        self.session.close()
        return result

from model.da.database import *
from model.entity import *

class LikeDa(DataBaseManager):
    def find_by_profile_id(self,profile_id):
        self.make_engine()
        result=self.session.query(Like).filter(Like.profile.id == profile_id)
        self.session.close()
        return result


    def find_by_post_id(self,post_id):
        self.make_engine()
        result = self.session.query(Like).filter(Like.post.id == post_id)
        self.session.close()
        return result


    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Like).filter(Like.profile.username == username)
        self.session.close()
        return result
    
    
    # def find_by_image(self, image):
    #     self.make_engine()
    #     result = self.session.query(Like).filter(Like.post.image == image)
    #     self.session.close()
    #     return result


    # todo : find_likes_count_by_profile_id



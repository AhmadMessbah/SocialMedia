from model.da.database import *
from model.entity.comment import Comment


class CommentDa(DataBaseManager):
    def find_by_profile_id(self, profile_id):
        self.make_engine()
        result = self.session.query(Comment).filter(Comment.profile.id == profile_id)
        self.session.close()
        return result

    def find_by_time(self, start_time, end_time):
        self.make_engine()
        result = self.session.query(Comment).filter(
            and_(Comment.date_time >= start_time, Comment.date_time <= end_time))
        self.session.close()
        return result


    def find_by_post_id(self,post_id):
        pass
        # self.make_engine()
        # todo : ---
        # self.session.close()
        # return result

    # todo : find_comments_count_by_profile_id

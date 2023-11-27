from model.da.database import *
from model.entity.comment import Comment


class CommentDa(DataBaseManager):
  def find_by_profile_id(self, profile_id):
        self.make_engine()
        result = self.session.query(Comment).filter(Comment.profile.id == profile_id)
        self.session.close()
        return result

  def find_by_time(self, datetime1, datetime2):
        self.make_engine()
        result = self.session.query(Comment).filter(and_(Comment.date_time >= datetime1, Comment.date_time <= datetime2))
        self.session.close()
        return result

from model.da import *
from model.entity import *

class CommentController:

    @classmethod
    def save(cls, post, profile):
        try:
            profile = post(None, profile, post)
            da = CommentDa()
            return True, da.save(post)
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, code, profile, post):
        try:
          like = Comment(code, profile, post)
          da = CommentDa()
          return True, da.edit(profile)
        except Exception as e:
              return False, str(e)

    @classmethod
    def remove(cls, code):
        try:
            da = CommentDa()
            return True, da.remove(code)
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_all(cls):
        try:
            da=CommentDa()
            return True,da.find_all()
        except Exception as e:
            return False,str(e)


    @classmethod
    def find_by_code(cls,code):
        try:
            da=CommentDa()
            return True,da.find_by_code(code)
        except Exception as e:
            return False,str(e)


    @classmethod
    def find_by_post(cls,post):
      try:
          da=CommentDa()
          return True,da.find_by_post(post)
      except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_profile(cls, profile):
      try:
           da = CommentDa()
           return True, da.find_by_profile_id(profile)
      except Exception as e:
           return False, str(e)


    @classmethod
    def find_by_username(cls, username):
      try:
          da = CommentDa()
          return True, da.find_by_username(username)
      except Exception as e:
          return False, str(e)


    @classmethod
    def find_by_time(cls, time):
        try:
            da = CommentDa()
            return True, da.find_by_image(time)
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_post_id(cls,postid):
        try:
            da=CommentDa()
            return True,da.find_by_podst_id(postid)
        except Exception as e:
            return False,str(e)
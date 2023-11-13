from model.da.like_da import likeDa
from model.entity.like import Post

class LikeController:

    @classmethod
    def save(cls, post, profile):
        try:
          person = post(None, profile, post)
          da = likeDa()
          return True, da.save(post)
        except Exception as e:
           return False, str(e)

    @classmethod
    def edit(cls, code, profile, post):
      try:
         person = likeDa(code, profile, post)
         da = likeDa()
         return True, da.edit(person)
      except Exception as e:
        return False, str(e)


    @classmethod
    def remove(cls, code):
      try:
        da = likeDa()
        return True, da.remove(code)
      except Exception as e:
         return False, str(e)


    @classmethod
    def find_all(cls):
      try:
        da = likeDa()
        return True, da.find_all()
      except Exception as e:
        return False, str(e)


    @classmethod
    def find_by_code(cls, code):
      try:
        da = likeDa()
        return True, da.find_by_code(code)
      except Exception as e:
        return False, str(e)


    @classmethod
    def find_by_post(cls, post):
       try:
          da =likeDa()
          return True, da.find_by_post(post)
       except Exception as e:
          return False, str(e)

    @classmethod
    def find_by_profile(cls,profile):
      try:
        da=likeDa()
        return True,da.find_by_profile_id(profile)
      except Exception as e:
        return False, str(e)

    @classmethod
    def find_by_username(cls,username):
       try:
         da=likeDa()
         return True,da.find_by_username(username)
       except Exception as e:
         return False, str(e)

def find_by_image(cls,image):
    try:
        da=likeDa
        return True,da.find_by_image(image)
    except Exception as e:
        return False,str(e)
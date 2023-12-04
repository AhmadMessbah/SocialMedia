from controller.exception.access_denied_error import AccessDeniedError
from controller.exception.duplicate_username_error import DuplicateUsernameError
from model.da.like_da import LikeDa
from model.entity.like import Like


class LikeController:
    @classmethod
    def save(cls, post, profile):
        try:
            da=LikeDa()
            if not da.find_by_post_id(post):
              like=Like(post,profile)
              da.save(like)
              return True, Like
        except Exception as e:
            return False , str(e)

    @classmethod
    def edit(cls, code, profile, post):
        try:
            da = LikeDa()
            if not da.find_by_post_id(post):
                like = Like( post, profile)
                da.edit(like)
                return True, Like
        except Exception as e:
            e.with_traceback()
            return False, str(e)
    @classmethod
    def remove(cls, code, profile, post):
        try:
            da = LikeDa()
            like = Like( post, profile)
            return True,  da.remove(like)
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_all(cls):
        try:
            da = LikeDa()
            return True, da.find_all(Like)
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_post(cls, post):
        try:
            da = LikeDa()
            return True, da.find_by_post(post)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_profile(cls, profile):
        try:
            da = LikeDa()
            return True, da.find_by_profile_id(profile)
        except Exception as e:
            return False, str(e)



def find_by_image(cls, image):
    try:
        da = LikeDa()
        return True, da.find_by_image(image)
    except Exception as e:
        return False, str(e)

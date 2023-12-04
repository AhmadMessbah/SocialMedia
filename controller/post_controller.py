from model.da import *
from model.entity import *

class PostController:
    @classmethod
    def save(cls, image, text):
        try:
            da = PostDa()
            post = Post(text, image)
            da.save(post)
            return post
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, profile_id, image, text):
        try:
            da = PostDa()
            post = Post(text, image)
            post.id = id
            post.profile_id = profile_id
            da.edit(post)
            return post
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = PostDa()
            post = da.find_by_id(Post, id)
            if post:
                da.remove(post)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(cls, datetime1, datetime2):
        try:
            da = PostDa()
            post_list = da.find_by_time(datetime1, datetime2)
            return post_list
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_profile_id(cls, profile_id):
        try:
            da = PostDa()
            post_list = da.find_by_profile_id(profile_id)
            return post_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_profile_username(cls, profile_username):
        try:
            da = PostDa()
            post_list = da.find_by_profile_username(profile_username)
            return post_list
        except Exception as e:
            return False, str(e)

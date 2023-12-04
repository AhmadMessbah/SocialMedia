from model.da.profile_da import ProfileDa
from model.entity.post import Post
from model.entity.profile import Profile
from model.da.post_da import PostDa


class PostController:
    @classmethod
    def save(self, profile_id, image, text):
        try:
            da = PostDa()
            # profile = da.find_by_id(Profile , profile_id)
            post = Post(text, image)
            da.save(post)
            return post
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(self, profile_id, image, text):
        try:
            da = PostDa()
            # profile = da.find_by_id(Profile, profile_id)
            post = Post( text, image)
            da.edit(post)
            return post
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(self, id):
        try:
            da = PostDa()
            post = da.find_by_id(Post, id)
            if post:
                da.remove(post)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(self, datetime1, datetime2):
        try:
            da = PostDa()
            post_list = da.find_by_time(datetime1, datetime2)
            return post_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_profile_id(self, profile_id):
        try:
            da = PostDa()
            post_list = da.find_by_profile_id(profile_id)
            return post_list
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_profile_id(self, profile_id):
        try:
            da = PostDa()
            post_list = da.find_by_profile_id(profile_id)
            return post_list
        except Exception as e:
            return False, str(e)
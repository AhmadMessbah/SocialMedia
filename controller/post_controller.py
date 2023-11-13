from model.da.profile_da import ProfileDa
from model.entity.post import Post
from model.entity.profile import Profile


class PostController:
    @classmethod
    def save(self,profile_id, image, text):
        try:
            da = ProfileDa()
            profile = da.find_by_id(Profile , profile_id)
            post = Post(profile, text, image)
            da.save(post)
            return post
        except Exception as e:
            return  False, str(e)
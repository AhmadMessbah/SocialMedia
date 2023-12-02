from model.da.database import *
from model.entity.comment import Comment
from model.entity.like import Like
from model.entity.post import Post
from model.entity.profile import Profile
#
da = DataBaseManager()

profile1 = Profile()
profile1.name = "post owner"
profile1.family = "post owner"
da.save(profile1)
print(profile1.id, profile1.name, profile1.family)

profile2 = Profile()
profile2.name = "comment-1"
profile2.family = "comment-1"
da.save(profile2)
print(profile2.id, profile2.name, profile2.family)

profile3 = Profile()
profile3.name = "comment2-like"
profile3.family = "comment2-like"
da.save(profile3)
print(profile3.id, profile3.name, profile3.family)

post1 = Post("man post1 haastam")
post1.profile_id = profile1.id
da.save(post1)

comment11 = Comment("man comment 1 - post1 hastam")
comment11.profile_id = profile3.id
comment11.post_id = post1.id
da.save(comment11)

like = Like()
like.post_id = post1.id
like.profile_id = profile3.id
da.save(like)

comment12 = Comment("man comment 2 - post1 hastam")
comment12.profile_id = profile2.id
comment12.post_id = post1.id
da.save(comment12)

profile = da.find_by_id(Profile, 1)
print(profile.name, profile.family)

for post in profile.posts:
    print("\tPOST :", post.id, post.text)
    for comment in post.comments:
        print("\t\tComment :", comment.id, comment.text, comment.profile.name)
#
    for like in post.likes:
        print("\t\tLike :",like.id, like.profile.name)

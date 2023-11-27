from model.da.database import *
from model.entity.comment import Comment
# from model.entity.like import Like
from model.entity.post import Post
from model.entity.profile import Profile

da = DataBaseManager()

profile1 = Profile()
profile1.name = "poster"
profile1.family = "poster"
da.save(profile1)
print(profile1.id, "saved")

profile2 = Profile()
profile2.name = "commenter1"
profile2.family = "commenter1"
da.save(profile2)
print(profile2.id, "saved")

profile3 = Profile()
profile3.name = "commenter-like2"
profile3.family = "commenter-like2"
da.save(profile3)
print(profile3.id, "saved")

post1 = Post()
post1.text = "man post1 haastam"
post1.profile_id = profile1.id
da.save(post1)

comment11 = Comment()
comment11.text = "man comment 1 - post1 hastam"
comment11.profile_id = profile3.id
comment11.post_id = post1.id
da.save(comment11)

# like = Like()
# like.post_id = post1.id
# like.profile_id = profile3.id
# da.save(like)

comment12 = Comment()
comment12.text = "man comment 2 - post1 hastam"
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
#     for like in post.likes:
#         print("\t\tLike :",like.id, like.profile.name)

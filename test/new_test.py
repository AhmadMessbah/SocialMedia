
from model.da import ProfileDa
from model.da.database import *




# profile_da = ProfileDa()
# print(profile_da.find_by_id(Profile, 1))

da = DataBaseManager()

profile1 = Profile("aaa111", "bbbb", "ahmad", "ahmad123")
print(profile1)
print(profile1.name)
da.save(profile1)
print(profile1.id, profile1.name, profile1.family)

post1 = Post(profile1, "man post1 hastam")
da.save(post1)
print(post1.id, post1.text)

comment1 = Comment(profile1, post1, "commmmmmmment")
da.save(comment1)
print(comment1.id, comment1.text)

#like1 = Like(profile1, post1)
#da.save(like1)
#print(like1.id)


profile_list = da.find_all(Profile)

# for pr in profile_list:
#     print("Profile : ", pr.id, pr.name, pr.family)
#
#     for ps in pr.posts:
#         print("\tPost : ", ps.id, ps.text)
#
#         for cm in ps.comments:
#             print("\t\tComment : ", cm.id, cm.text, cm.profile.name)
#
#         for lk in ps.likes:
#             print("\t\tLikes : ", lk.id, lk.profile.name)

# username = input("Enter Username : ")
# da.make_engine()
# result = da.session.query(Profile).filter(Profile.username == username).all()
# print(result)
#
# for r in result:
#     print(r.name,r.family)


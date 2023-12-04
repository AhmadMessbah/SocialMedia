from controller.profile_controller import ProfileController
from model.da.profile_da import ProfileDa
from model.entity import Profile

da = ProfileDa()
# for pr in da.find_all(Profile):
#     print(pr.json())

# print(da.find_by_id(Profile,1).json())
user = da.find_by_username("ahmad")
print(user.posts)
# print(da.find_by_username_password("aa","bb111").json())

# print(ProfileController.save("aaa", "bbbb", "aaeeee", "1231"))
# print(ProfileController.login("zzzz@zzz.com", "zzzz"))
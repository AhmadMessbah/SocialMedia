from controller.profile_controller import ProfileController
from model.da.profile_da import ProfileDa
from model.entity import Profile

# da = ProfileDa()
# for pr in da.find_all(Profile):
#     print(pr.json())

# print(da.find_by_id(Profile,1).json())
# print(da.find_by_username("aa").json())
# print(da.find_by_username_password("aa","bb111").json())

# print(ProfileController.save("aaa", "bbbb", "aaeeee", "1231"))
print(ProfileController.login("aaeeeewerwerwerw", "1231"))
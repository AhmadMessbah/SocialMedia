from model.da import ProfileDa
from model.entity import Profile

profile = Profile("Ahmad","Messbah","aaa", "bbb")
profile_da = ProfileDa()
profile_da.save(profile)

print(profile.id)
print(profile.name)
print(profile.family)
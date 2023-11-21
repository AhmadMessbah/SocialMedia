from controller.profile_controller import ProfileController
from model.da.database import DatabaseManager
from model.entity.profile import Profile

# db = DatabaseManager()
# p = Profile("a","b","c","d")
# p = db.save(p)

print(ProfileController.remove(1))

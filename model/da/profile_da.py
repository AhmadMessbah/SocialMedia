from model.da.database import DatabaseManager
from model.entity.profile import Profile

class ProfileDa(DatabaseManager):
     def find_by_family(self, family):
        self.make_engine()
        result = self.session.query(Profile).filter(Profile.family.like(family+"%"))
        self.session.close()
        return result
from model.da.profile_da import ProfileDa
from model.entity.profile import Profile



class PersonController:
    @classmethod
    def find_by_family(cls, family):
        try:
            da = ProfileDa()
            return True, da.find_by_family(family)
        except Exception as e:
            return False, str(e)
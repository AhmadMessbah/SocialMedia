

from model.da.profile_da import ProfileDa
from model.entity.profile import Profile


class PersonController:
    @classmethod
    def save(cls, name, family):
        try:
            profile = Profile(None, name, family)
            da = ProfileDa()
            return True, da.save(profile)
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, code, name, family):
        try:
            person = Profile(code, name, family)
            da = ProfileDa()
            return True, da.edit(Profile)
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, code):
        try:
            da = ProfileDa()
            return True, da.remove(code)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProfileDa()
            return True, da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_code(cls, code):
        try:
            da = ProfileDa()
            return True, da.find_by_code(code)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls, family):
        try:
            da = ProfileDa()
            return True, da.find_by_family(family)
        except Exception as e:
            return False, str(e)
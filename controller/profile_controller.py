from controller.access_denied_error import AccessDeniedError
from controller.exception.duplicate_username_error import DuplicateUsernameError
from model.da.profile_da import ProfileDa
from model.entity.profile import Profile


class ProfileController:
    @classmethod
    def save(cls, name, family, username, password):
        try:
            da = ProfileDa()
            # todo : check duplicate user name first
            # if (da.find_by_username(username) or not da.find_by_username(username)[0]):
            profile = Profile(name, family, username, password)
            da.save(profile)
            return True, profile
            # else:
            #     raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls,id):
        try:
            da = ProfileDa()
            profile = da.find_by_id(Profile,id)
            return True, da.remove(profile)
        except Exception as e:
            return False, str(e)


    @classmethod
    def login(cls, username, password):
        try:
            da = ProfileDa()
            profile = da.find_by_username_password(username,password)
            if (profile):
                return True, profile
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProfileDa()
            return True, da.find_all(Profile)
        except Exception as e:
            return False, str(e)

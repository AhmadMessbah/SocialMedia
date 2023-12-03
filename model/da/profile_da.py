from model.da.database import *
from model.entity.profile import Profile


class ProfileDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Profile).filter(and_(Profile.username == username, Profile.password == password))
        return result


    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Profile).filter(Profile.username == username)
        try:
            if (result.username):
                return result
        except:
            return None

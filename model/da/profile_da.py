from model.da.database import *
from model.entity.profile import Profile


class ProfileDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Profile).filter(and_(Profile.username == username, Profile.password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Profile).filter(Profile.username == username).all()
        if result:
            return result[0]

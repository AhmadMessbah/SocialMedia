from model.da.database import DataBaseManager,and_,or_,between
from model.entity import *


class ProfileDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Profile).filter(
            and_(Profile.username == username, Profile.password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Profile).filter(Profile.username == username).all()
        if result:
            return result[0]

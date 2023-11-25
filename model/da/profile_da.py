from model.da.database import DatabaseManager
from model.entity.profile import Profile

class ProfileDa(DatabaseManager):
        def find_by_username_password(self, username, password):
             self.make_engine()
             result = self.session.query(Profile).filter(
                 and_(Profile.username == username, Profile.password == password))
             self.session.close()
             return result

     def find_by_username(self, username):
         self.make_engine()
         result = self.session.query(Profile).filter(Profile.username == username)
         try:
             if (result.username):
                 self.session.close()
                 return result
         except:
             return None


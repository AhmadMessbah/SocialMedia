from model.entity.profile import Profile
from tools.database import Database


class ProfileDa(Database):
    def save(self, profile):
        sql_command = "INSERT INTO profile (name, family, username, password, email, image, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (profile.name, profile.family, profile.username, profile.password, profile.email, profile.image, profile.status)
        self.execute_sql(sql_command, data)
        return profile

    def edit(self, profile):
        sql_command = "UPDATE profile SET name=%s, family=%s, username=%s, password=%s, email=%s, image=%s, status=%s WHERE CODE=%s"
        data = (profile.name, profile.family, profile.username, profile.password, profile.email, profile.image, profile.status, profile.code)
        self.execute_sql(sql_command, data)
        return profile

    def remove(self, code):
        sql_command = "DELETE FROM profile WHERE CODE=%s"
        data = (code,)
        self.execute_sql(sql_command, data)
        return code

    def find_all(self):
        sql_command = "SELECT * FROM profile"
        return self.fetch_all_results(sql_command)

    def find_by_code(self, code):
        sql_command = "SELECT * FROM profile WHERE CODE=%s"
        data = (code,)
        return self.fetch_all_results(sql_command, data)

    def find_by_family(self, family):
        sql_command = "SELECT * FROM profile WHERE FAMILY=%s"
        data = (family,)
        return self.fetch_all_results(sql_command, data)

#a = ProfileDa()
#b = Profile(2,'mamad','masumi','reza','behna','behnamlive@live.com','behhh',1)
#a.save(b)
#a.edit(b)
#a.remove(2)
from profile import Profile

from tools.database import Database




class ProfileDa(Database):
    def save(self, profile):
        Database.connect()
        self.transaction("INSERT INTO profile (name,family,username,password,email,image,status) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                         [profile.name,profile.family,profile.username,profile.password,profile.email,profile.image,profile.status])
        Database.transaction()
        Database.disconnect()
        return profile

    def edit(self, profile):
        Database.connect()
        self.transaction("UPDATE profile SET name=%s,family=%s,username=%s,password=%s,email=%s,image=%s,status=%s WHERE CODE=%s",
                         [profile.name,profile.family,profile.username,profile.password,profile.email,profile.image,profile.status])
        Database.transaction()
        Database.disconnect()
        return profile

    def remove(self, code):
        self.transaction("delete from profile where code=%s, WHERE CODE=%s",
                         [code,code])
        return code

    def find_all(self):
        return self.report("SELECT * FROM profile")


    def find_by_code(self, code):
        return self.report("SELECT * FROM profile WHERE CODE=%s", [code])

    def find_by_family(self, family):
        return self.report("SELECT * FROM profile WHERE FAMILY=%s ", [family])

a = ProfileDa()


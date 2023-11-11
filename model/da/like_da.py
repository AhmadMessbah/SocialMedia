from tools.database import Database
from model.entity import  like

class likeDa(Database):
    def save(self, like):
        self.transaction("INSERT INTO like_tbl (profile,post) values (%s,%s)",
                          [like.profile,like.post])
        return like

    def edit(self, like):
        self.transaction("UPDATE like_tbl set profile=%s,post=%s  where  code=%s"
                         ,[like.profile,like.post])
        return like


    def remove(self, code):
        self.transaction("DELETE FROM like_tbl where code=%s",
                         [code])
        return code

    def find_all(self):
        return self.report("SELECT * FROM like_tbl")


    def find_by_code(self, code):
        return self.report("SELECT * FROM like_tbl where code=%s",[code])

    def find_by_profile(self,profile):
        return self.report("SELECT * FROM like_tbl where profile=%s",[like.profile])


    def find_by_post(self,post):
        return self.report("SELECT * FROM like_tbl where post=%s",[like.post])





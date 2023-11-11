from tools.database import Database
from model.entity import  like

class likeDa(Database):
    def save(self, like):
        self.transaction("INSERT INTO like_tbl (profile_id,post_id) values (%s,%s)",
                          [like.profile_id,like.post_id])
        return like

    def edit(self, like):
        self.transaction("UPDATE like_tbl set profile_id=%s,post_id=%s  where  code=%s"
                         ,[like.profile,like.post_id])
        return like


    def remove(self, code):
        self.transaction("DELETE FROM like_tbl where code=%s",
                         [code])
        return code

    def find_all(self):
        return self.report("SELECT * FROM like_tbl")


    def find_by_code(self, code):
        return self.report("SELECT * FROM like_tbl where code=%s",[code])

    def find_by_profile_id(self,profile):
        return self.report("SELECT * FROM like_tbl where profile_id=%s",[like.profile_id])


    def find_by_post_id(self,post_id):
        return self.report("SELECT * FROM like_tbl where post_id=%s",[like.post_id])



    def find_by_username(self,username):
        return self.report("SELECT * FROM like_tbl where username_id=%s",[like.username])
    
    
    def find_by_image(self):
        return self.report("SELECT * FROM like_tbl where image=%s",[like.image])





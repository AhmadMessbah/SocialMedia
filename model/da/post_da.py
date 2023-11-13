from tools.database import Database
from model.entity import  post

class PostDa(Database):
    def save(self, post):
        self.transaction("INSERT INTO post_tbl (profile_id,text,image) values (%s,%s,%s)",
                          [post.profile.code, post.text, post.image])
        return post

    def edit(self, post):
        self.transaction("UPDATE post_tbl set text=%s,image=%s  where  code=%s"
                         , [post.text, post.image, post.code])
        return post


    def remove(self, code):
        self.transaction("DELETE FROM post_tbl where code=%s",
                         [code])
        return code

    def find_all(self):
        return self.report("SELECT * FROM post_tbl")


    def find_by_code(self, code):
        return self.report("SELECT * FROM post_tbl where code=%s", [code])

    def find_by_profile(self,profile):
        return self.report("SELECT * FROM post_tbl where profile_id=%s", [post.profile.code])



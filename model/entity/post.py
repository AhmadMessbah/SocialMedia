
class Post:
    def __init__(self,code,profile,text,image,date_time):
        self.code = code
        self.profile = profile
        self.text = text
        self.image = image
        self.date_time = date_time

    def __repr__(self):
        return str(self.__dict__)

    def convert_to_tuple(self):
        return self.code ,self.name ,self.family


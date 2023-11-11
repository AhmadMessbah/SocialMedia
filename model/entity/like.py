class Post:
    def __init__(self, code, post, profile):
        self.code=code
        self.post=post
        self.profile=profile

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

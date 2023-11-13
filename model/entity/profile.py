import re
from sqlalchemy import Integer, String, Boolean, Date, ForeignKey, Column
from sqlalchemy.orm import relationship

from model.entity.base import Base
from tools.validator import Validator


class Profile(Base):
    __tablename__ = "profile_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))
    email = Column(String(30))
    image = Column(String(100))
    status = Column(Boolean)

    def __init__(self, id, name, family, username, password, email, image, status):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.email = email
        self.image = image
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        Validator.is_number(id, True, "Invalid Code")
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and re.match("^[a-zA-Z\s]{2,30}$", name):
            self._name = name
        else:
            raise ValueError("invalid name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if isinstance(family, str) and re.match("^[a-zA-Z\s]{2,30}$", family):
            self._family = family
        else:
            raise ValueError("invalid family")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and re.match("^[a-zA-Z\s]{2,30}$", username):
            self._username = username
        else:
            raise ValueError("invalid username")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and re.match("^[a-zA-z\d\-\+\-]+@+[a-zA-Z\d\-\+\-]+\.{1}[a-zA-Z]{2,6}+$", email):
            self._email = email
        else:
            raise ValueError("invalid email")

    def __repr__(self):
        return str(self.__dict__)

    def to_tuple(self):
        return tuple(self.__dict__.values())

a =Profile(1,'behnam','masoumi','behnamlive','behnam12','behnamlive@live.com','asasd',1)
print(Profile.to_tuple(a))

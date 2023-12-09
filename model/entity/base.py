import json
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def to_json(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})

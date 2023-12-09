from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        return str({c.key[1:] if c.key.startswith("_") else c.key : getattr(self, c.key) for c in inspect(self).mapper.column_attrs})


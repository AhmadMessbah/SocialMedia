from sqlalchemy import create_engine,and_,or_, between
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from model.entity.base import Base


class DataBaseManager:
    def make_engine(self):
        if not database_exists("mysql+pymysql://root:root123@localhost:3306/mft"):
            create_database("mysql+pymysql://root:root123@localhost:3306/mft")

        self.engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, entity):
        self.make_engine()
        entity = self.session.add(entity)
        self.session.commit()
        return entity

    def edit(self, entity):
        self.make_engine()
        entity = self.session.merge(entity)
        self.session.commit()
        return entity

    def remove(self, entity):
        # todo : make it logically remove
        self.make_engine()
        entity = self.session.delete(entity)
        self.session.commit()
        return entity

    def find_all(self, class_name):
        # todo : find_all un deleted
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        return entity_list

    def find_by_id(self, class_name, id):
        # todo : find_all un deleted
        self.make_engine()
        entity = self.session.get(class_name, id)
        return entity

    def find_by(self, class_name, search_filter):
        # todo : find_all un deleted
        self.make_engine()
        entity = self.session.query(class_name).filter(search_filter)
        return entity

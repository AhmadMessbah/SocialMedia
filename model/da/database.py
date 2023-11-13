import time

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import text, and_, or_

from model.entity.base import Base

from sqlalchemy.orm import sessionmaker


import sqlalchemy_utils
from sqlalchemy_utils import database_exists, create_database


# engine = create_engine('mysql+pymysql://root:root123@localhost:3306/mft', echo=True)

class DatabaseManager:
    def make_engine(self):
        if not database_exists('mysql+pymysql://root:root123@localhost:3306/mft'):
            create_database('mysql+pymysql://root:root123@localhost:3306/mft')
        self.engine = create_engine('mysql+pymysql://root:root123@localhost:3306/mft')

        # Create Tables
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, entity):
        self.make_engine()
        entity = self.session.add(entity)
        self.session.commit()
        self.session.close()
        return entity

    def edit(self, entity):
        self.make_engine()
        entity = self.session.merge(entity)
        self.session.commit()
        self.session.close()
        return entity

    def remove(self, entity):
        self.make_engine()
        entity = self.session.delete(entity)
        self.session.commit()
        self.session.close()
        return entity

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        self.session.close()
        return entity_list


    def find_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        self.session.close()
        return entity



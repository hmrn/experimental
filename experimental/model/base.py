from __future__ import absolute_import

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column
from sqlalchemy.ext import declarative
from sqlalchemy.types import BigInteger, DateTime


engine = create_engine('mysql+mysqldb://hmrn:hmrn@localhost:3306')
session = scoped_session(sessionmaker(bind=engine))


def get_session():
    return session


class Model(object):
    @classmethod
    def query(cls, *args, **kwargs):
        return get_session().query(cls, *args, **kwargs)

    @declarative.declared_attr
    def id(self):
        return Column('id', BigInteger, primary_key=True, autoincrement=True)

    @declarative.declared_attr
    def created_at(self):
        """
        Audit field, shouldn't be used of manipulated
        """
        return Column('created_at', DateTime(timezone=True), default=func.now(), nullable=False)

    def update(self):
        get_session().flush()
        get_session().refresh(self)


Base = declarative.declarative_base(cls=Model)

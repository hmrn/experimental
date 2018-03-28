from __future__ import absolute_import

from sqlalchemy.schema import Column
from sqlalchemy.types import String

from experimental.model.base import Base, get_session


class DemoModelOverWriteException(Exception):
    def __init__(self, name):
        super(DemoModelOverWriteException, self).__init__(
            "demo model instance '{}' already exists".format(name)
        )


class DemoModel(Base):
    __tablename__ = "demo_model"

    name = Column("name", String(160), unique=True, index=True, nullable=False)

    @classmethod
    def get_by_name(cls, name):
        return cls.query().filter(cls.name == str(name)).first()

    @classmethod
    def new(cls, name):
        if cls.get_by_name(name):
            raise DemoModelOverWriteException(name)
        obj = cls(name=name)
        get_session().add(obj)
        return obj

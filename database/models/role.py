from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from typing import Optional
from flask_security import RoleMixin
from ..database import Base
from .crud import CRUD


class Role(Base.Model, CRUD, RoleMixin):

    __tablename__ = 'role'

    name = Column(String(255),unique=True, nullable=False)

    def __init__(self, name: str = None, id: Optional[uuid.UUID] = None, deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.name = name

    def __repr__(self):
        return self.name

from sqlalchemy import Column, ForeignKey, Integer, DateTime, JSON
from datetime import datetime as python_datetime
from ..database import Base
from .crud import CRUD
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import uuid


class Purchase(CRUD, Base.Model,):
    __tablename__ = 'purchase'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))
    datetime = Column(DateTime, nullable=False, unique=False)
    cost = Column(Integer, nullable=True, unique=False)
    about = Column(JSON, nullable=False, unique=False)

    def __init__(self, datetime: Optional[python_datetime] = None,
                 cost: Optional[int] = None,
                 about: Optional[str] = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.datetime = datetime
        self.cost = cost
        self.about = about


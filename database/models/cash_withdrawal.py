from sqlalchemy import Column, ForeignKey, JSON, DateTime, Integer, Boolean
from datetime import datetime as python_datetime
from ..database import Base
from .crud import CRUD
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import uuid


class CashWithdrawal(CRUD, Base.Model):
    __tablename__ = 'cash_withdrawal'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))
    datetime = Column(DateTime, nullable=False, unique=False)
    amount = Column(Integer, nullable=False, unique=False)
    information = Column(JSON, nullable=False, unique=False)
    is_done = Column(Boolean, nullable=False, unique=False)
    executor_id = Column(UUID(as_uuid=True), nullable=False, unique=False)

    def __init__(self, datetime: Optional[python_datetime] = None,
                 amount: Optional[int] = None,
                 information: Optional[str] = None,
                 is_done: Optional[bool] = None,
                 executor_id: Optional[uuid.UUID] = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.datetime = datetime
        self.amount = amount
        self.information = information
        self.is_done = is_done
        self.executor_id = executor_id
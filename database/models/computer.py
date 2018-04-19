from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.dialects.postgresql import UUID

import uuid
from typing import Optional

from ..database import Base
from .crud import CRUD


class Computer(Base.Model, CRUD):
    __tablename__ = 'computer'

    mask = Column(String(256), nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))

    def __init__(self, mask: str, id: Optional[uuid.UUID] = None, deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.mask = mask



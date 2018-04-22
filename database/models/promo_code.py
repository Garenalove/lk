from sqlalchemy import Column, ForeignKey, JSON, DateTime, String
from datetime import datetime
from ..database import Base
from .crud import CRUD
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import uuid


class PromoCode(CRUD, Base.Model):
    __tablename__ = 'promo_code'

    name = Column(String(255), nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))
    effect = Column(JSON, nullable=False, unique=False)
    end_time = Column(DateTime, nullable=False, unique=False)

    def __init__(self, name: Optional[str] = None,
                 effect: Optional[str] = None,
                 end_time: Optional[datetime] = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.name = name
        self.effect = effect
        self.end_time = end_time
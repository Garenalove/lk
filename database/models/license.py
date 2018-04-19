from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timedelta
import uuid
from typing import Optional
from .addon import Addon

from ..database import Base
from .crud import CRUD


class License(Base.Model, CRUD):
    __tablename__ = 'license'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))
    addon_id = Column(UUID(as_uuid=True),ForeignKey('addon.id'))
    addon = relationship('Addon', backref='license', uselist=False)
    end_time = Column(DateTime, nullable=True, unique=False)

    def __init__(self, addon:Addon, id: Optional[uuid.UUID] = None, deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.addon = addon
        self.end_time = datetime.now() + timedelta(days=addon.period)
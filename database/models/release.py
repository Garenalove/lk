from sqlalchemy import Column, ForeignKey, String   , Integer, Boolean
from ..database import Base
from .crud import CRUD
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import uuid


class Release(CRUD, Base.Model):
    __tablename__ = 'release'

    version = Column(String(255), nullable=False, unique=False)
    cost = Column(Integer, nullable=False, unique=False)
    path = Column(String(255), nullable=False, unique=True)
    can_be_sell = Column(Boolean, nullable=False, unique=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('product.id'))

    def __init__(self, version: Optional[str] = None,
                 cost: Optional[str] = None,
                 path: Optional[str] = None,
                 can_be_sell: Optional[bool] = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.version = version
        self.cost = cost
        self.path = path
        self.can_be_sell = can_be_sell

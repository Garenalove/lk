from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timedelta
import uuid
from typing import Optional
from .product import Product

from ..database import Base
from .crud import CRUD


class License(Base.Model, CRUD):
    __tablename__ = 'license'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user_.id'))
    product_id = Column(UUID(as_uuid=True),ForeignKey('product.id'))
    product = relationship('Product', backref='license', uselist=False)
    end_time = Column(DateTime, nullable=True, unique=False)

    def __init__(self, product:Product, id: Optional[uuid.UUID] = None, deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.product = product
        self.end_time = datetime.now() + timedelta(days=product.release)
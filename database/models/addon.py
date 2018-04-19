from sqlalchemy import Column, String, Float, Integer
import uuid
from typing import Optional
from utils.utlis import translate
from ..database import Base
from .crud import CRUD
import re


class Addon(Base.Model, CRUD):
    __tablename__ = 'addon'

    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256), nullable=False, unique=False)
    cost = Column(Float, nullable=False, unique=False)
    period = Column(Integer, nullable=False, unique=False)
    slug = Column(String(256), nullable=False, unique=True)

    def __init__(self,
                 name: str = None,
                 description: str = None,
                 cost: float = None,
                 period: int = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.name = name
        self.description = description
        self.cost = cost
        self.period = period
        if self.slug:
            self.generate_slug()

    def generate_slug(self):
        self.slug = re.sub(r'[^\w+]', '-', translate(self.name.lower()))

    def __repr__(self):
        return self.name

from sqlalchemy import Column, String, Float, JSON
import uuid
from typing import Optional
from utils.utlis import translate
from ..database import Base
from .crud import CRUD
import re


class Product(Base.Model, CRUD):
    __tablename__ = 'product'

    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256), nullable=False, unique=False)
    cost = Column(Float, nullable=False, unique=False)
    release = Column(JSON, nullable=False, unique=False)
    link = Column(String(256), nullable=False, unique=True)

    def __init__(self,
                 name: str = None,
                 description: str = None,
                 cost: float = None,
                 release: str = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.name = name
        self.description = description
        self.cost = cost
        self.release = release
        if self.link:
            self.generate_link()

    def generate_link(self):
        self.link = re.sub(r'[^\w+]', '-', translate(self.name.lower()))

    def __repr__(self):
        return self.name

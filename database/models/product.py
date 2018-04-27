from sqlalchemy import Column, String, Float, JSON
import uuid
from typing import Optional
from sqlalchemy.orm import relationship
from utils.utlis import translate
from ..database import Base
from .crud import CRUD
import re


class Product(Base.Model, CRUD):
    __tablename__ = 'product'

    name = Column(String(256), nullable=False, unique=True)
    description = Column(String(256), nullable=False, unique=False)
    cost = Column(Float, nullable=False, unique=False)
    releases = relationship('Release', backref='product')
    link = Column(String(256), nullable=False, unique=True)

    def __init__(self,
                 name: str = None,
                 description: str = None,
                 cost: int = None,
                 link: str = None,
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.name = name
        self.description = description
        self.cost = cost
        self.releases = []
        if link:
            self.link = link
        else:
            if self.name:
                self.generate_link()

    def generate_link(self):
        self.link = re.sub(r'[^\w+]', '-', translate(self.name.lower()))

    def __repr__(self):
        return self.name

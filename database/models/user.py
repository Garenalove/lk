from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .computer import Computer
from .addon import Addon
import uuid
from typing import Optional, List
from ..database import Base
from .crud import CRUD
from flask_security import UserMixin
from sqlalchemy.dialects.postgresql import UUID


role_user = Base.Table(
    'role_user',
    Column('role_id', UUID(as_uuid=True), ForeignKey('role.id'), nullable=False),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user_.id'), nullable=False),
)


class User(CRUD, Base.Model, UserMixin):
    __tablename__ = 'user_'

    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False, unique=False)
    balance = Column(Float, nullable=True, unique=False, default=float(0))
    active = Column(Base.Boolean())
    computers = relationship('Computer', backref='user_')
    licenses = relationship('License', backref='user_')
    roles = relationship('Role', secondary=role_user, backref='user_')
    computers_limit = Column(Integer, nullable=False, unique=False)

    def __init__(self, email: str = None,
                 password: str = None,
                 balance: float = None,
                 active: Optional[bool] = True,
                 roles: Optional[list] = list(),
                 id: Optional[uuid.UUID] = None,
                 deleted: Optional[bool] = None):
        CRUD.__init__(self, id, deleted)
        self.computers = []
        self.licenses = []
        self.email = email
        self.password = password
        self.balance = balance
        self.computers_limit = 3
        self.roles = roles
        self.active = active

    def buy_computer_slot(self):
        self.computers_limit += 1

    def add_computer(self, computer: Computer) -> bool:
        if self.computers.__len__() < self.computers_limit:
            self.computers.append(computer)
            return True
        return False

    def is_addon(self, addon: Addon):
        for license_ in self.licenses:
            if license_.addon.__eq__(addon):
                return license_
        return None

    def __repr__(self):
        return self.email

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base


role_user = Base.Table(
    'role_user',
    Column('role_id', UUID(as_uuid=True), ForeignKey('role.id'), nullable=False),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user_.id'), nullable=False),
)
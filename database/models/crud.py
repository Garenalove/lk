from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.postgresql import UUID

import uuid
from typing import Optional

from database.database import session


class CRUD(object):
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
    deleted = Column(Boolean, default=False, nullable=False)

    def __init__(self, id: Optional[uuid.UUID] = None, deleted: Optional[bool] = None):
        self.id = id
        self.deleted = deleted

    def create(self):
        session.add(self)
        session.commit()
        return self

    def delete(self):
        self.deleted = True
        session.commit()
        return self

    def update(self):
        session.commit()
        return self

    def __eq__(self, other: 'CRUD') -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
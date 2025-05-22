import uuid

from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base  # Importe a Base central

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_external_id = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False, )

    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan", single_parent=True)
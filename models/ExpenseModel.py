import uuid

from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base  # Importe a Base central

class Expense(Base):
    __tablename__ = "expenses"
    expense_id = Column(Integer, primary_key=True, autoincrement=True)
    expense_external_id = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    amount = Column(Integer)
    user_external_id = Column(UUID(as_uuid=True), ForeignKey("users.user_external_id"), nullable=False)

    user = relationship("User", back_populates="expenses")
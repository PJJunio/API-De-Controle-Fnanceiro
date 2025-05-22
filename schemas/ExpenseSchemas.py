from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID as PythonUUID

class ExpenseOutput(BaseModel):
    expense_external_id: PythonUUID
    name: str
    description: Optional[str] = None
    amount: float
    user_external_id: PythonUUID

class ExpenseCreateInput(BaseModel):
    user_external_id: PythonUUID
    name: str
    description: str | None = None
    amount: float

class ExpenseDeleteInput(BaseModel):
    user_external_id: PythonUUID
    expense_external_id: PythonUUID

class ExpenseUpdateInput(BaseModel):
    user_external_id: PythonUUID
    expense_external_id: PythonUUID
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None

class StandartExpenseOutput(BaseModel):
    message: str

class ExpenseListOutput(BaseModel):
    expenses: List[ExpenseOutput]
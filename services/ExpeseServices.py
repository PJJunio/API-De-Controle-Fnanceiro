from typing import List

from fastapi import HTTPException
from sqlalchemy import delete, select, update

from database.connection import async_session
from models.ExpenseModel import Expense
from uuid import UUID as PythonUUID

from schemas.ExpenseSchemas import ExpenseUpdateInput


class ExpenseService:
    async def create_expense(user_external_id: PythonUUID, name: str, description: str, amount: int):
        async with async_session() as session:
            session.add(Expense(user_external_id=user_external_id, name=name, description=description, amount=amount))
            await session.commit()

    async def delete_expense(user_external_id: PythonUUID, expense_external_id: PythonUUID):
        async with async_session() as session:
            result = await session.execute(
                delete(Expense).where(
                    Expense.expense_external_id == expense_external_id,
                    Expense.user_external_id == user_external_id
                )
            )
            await session.commit()
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Expense not found for this user")

    async def list_expenses(user_external_id: PythonUUID) -> List[Expense]:
        async with async_session() as session:
            result = await session.execute(
                select(Expense).where(Expense.user_external_id == user_external_id)
            )
            expenses = result.scalars().all()
            return list(expenses)

    async def update_expense(self, expense_update_input: ExpenseUpdateInput):
        async with async_session() as session:
            update_data = expense_update_input.model_dump(
                exclude_unset=True)

            user_external_id = update_data.pop("user_external_id")
            expense_external_id = update_data.pop("expense_external_id")

            if not update_data:
                raise HTTPException(status_code=400, detail="No fields provided for update")
            result = await session.execute(
                update(Expense)
                .where(
                    Expense.expense_external_id == expense_external_id,
                    Expense.user_external_id == user_external_id
                )
                .values(**update_data)
            )
            await session.commit()
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Expense not found or not owned by this user")
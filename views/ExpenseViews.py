from fastapi import APIRouter, HTTPException, Depends

from schemas.ExpenseSchemas import ExpenseCreateInput, StandartExpenseOutput, ExpenseDeleteInput, ExpenseListOutput, \
    ExpenseOutput, ExpenseUpdateInput
from services.ExpeseServices import ExpenseService
from uuid import UUID as PythonUUID

expenses_router = APIRouter(prefix="/expenses")

def get_expense_service():
    return ExpenseService()

@expenses_router.post("/create", response_model=StandartExpenseOutput)
async def create_expense(expense_input: ExpenseCreateInput):
    try:
        await ExpenseService.create_expense(
            user_external_id=expense_input.user_external_id,
            name=expense_input.name,
            description=expense_input.description,
            amount=expense_input.amount
        )
        return StandartExpenseOutput(message=f"Expense {expense_input.name} created")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@expenses_router.delete("/delete", response_model=StandartExpenseOutput)
async def delete_expense(expense_delete_input: ExpenseDeleteInput):
    try:
        await ExpenseService.delete_expense(
            user_external_id=expense_delete_input.user_external_id,
            expense_external_id=expense_delete_input.expense_external_id
        )
        return StandartExpenseOutput(message="Expense deleted successfully")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@expenses_router.get("/list/{user_external_id}", response_model=ExpenseListOutput)
async def list_expenses_by_user(user_external_id: str):
    try:
        expenses = await ExpenseService.list_expenses(user_external_id=PythonUUID(user_external_id))
        expense_outputs = [
            ExpenseOutput(
                expense_external_id=expense.expense_external_id,
                name=expense.name,
                description=expense.description,
                amount=expense.amount,
                user_external_id=expense.user_external_id
            )
            for expense in expenses
        ]
        return ExpenseListOutput(expenses=expense_outputs)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@expenses_router.put("/edit", response_model=StandartExpenseOutput)
async def edit_expense(
    expense_update_input: ExpenseUpdateInput,
    expense_service: ExpenseService = Depends(get_expense_service)
):
    try:
        await expense_service.update_expense(expense_update_input=expense_update_input)
        return StandartExpenseOutput(message="Expense updated successfully")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
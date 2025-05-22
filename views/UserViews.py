from fastapi import APIRouter, HTTPException, Depends

from schemas.UserSchemas import UserCreateInput, UserListOutput, StandartUserOutput
from services.UserServices import UserService
from uuid import UUID as PythonUUID

user_router = APIRouter(prefix="/users")

async def get_user_service() -> UserService:
    return UserService()

@user_router.post("/create", response_model=StandartUserOutput)
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(email=user_input.email, password=user_input.password)
        return StandartUserOutput(message="User created successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.delete("/delete/{user_external_id}", response_model=StandartUserOutput)
async def delete_user_route(user_external_id: str):
    try:
        await UserService().delete_user(user_external_id=PythonUUID(user_external_id))
        return StandartUserOutput(message=f"User {user_external_id} and associated data deleted successfully")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/list", response_model=list[UserListOutput])
async def get_all_users(user_service: UserService = Depends(get_user_service)):
    try:
        users = await user_service.list_users()
        return [UserListOutput(user_id=user.user_id, email=user.email) for user in users]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
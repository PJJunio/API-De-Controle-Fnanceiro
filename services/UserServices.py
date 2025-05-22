from fastapi import HTTPException
from sqlalchemy import Select, delete, select

from database.connection import async_session
from models.UserModel import User
from uuid import UUID as PythonUUID


class UserService:
    async def create_user(email: str, password: str):
        async with async_session() as session:
            session.add(User(email=email, password=password))
            await session.commit()

    async def delete_user(self, user_external_id: PythonUUID):
        async with async_session() as session:
            result = await session.execute(
                delete(User).where(User.user_external_id == user_external_id)
            )
            await session.commit()
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    async def list_users():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()
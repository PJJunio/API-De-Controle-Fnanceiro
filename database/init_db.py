from asyncio import run

from database.connection import engine, DATABASE_URL
from database.base import Base
from models.UserModel import User
from models.ExpenseModel import Expense

async def create_db():
    print(f"Tentando conectar ao banco de dados: {DATABASE_URL}")
    async with engine.begin() as connection:
        print("Conexão bem-sucedida.")
        print("Criando tabelas...")
        await connection.run_sync(Base.metadata.create_all)
        print("Tabelas criadas.")

        # Adicione este bloco para inspecionar as tabelas na metadata
        print("\nTabelas registradas na Base.metadata:")
        for table_name in Base.metadata.tables.keys():
            print(f"- {table_name}")

if __name__ == "__main__":
    run(create_db())
    print("Script de inicialização finalizado.")
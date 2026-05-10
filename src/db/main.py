from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from src.config import Config
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase



engine=create_async_engine(Config.DATABASE_URL,echo=True)

AsyncSessionLocal=async_sessionmaker(engine,expire_on_commit=False,class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def init_db():
    async with engine.begin() as conn:
        statement=text("SELECT 'hello';")

        result=await conn.execute(statement)

        print(result.all())
        
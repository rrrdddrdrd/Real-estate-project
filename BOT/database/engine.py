from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from database.module import Registration, RegistrationHouse, Status
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_async_engine(os.getenv('BB_LITE'))

session_marker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def crate_db():
    async with engine.begin() as conn:
        await conn.run_sync(Registration.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Registration.metadata.drop_all)

async def crate_db_house():
    async with engine.begin() as conn:
        await conn.run_sync(RegistrationHouse.metadata.create_all)

async def crate_db_status():
    async with engine.begin() as conn:
        await conn.run_sync(Status.metadata.create_all)


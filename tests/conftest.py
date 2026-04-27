import asyncio

import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import get_db
from app.db.base import BaseModel

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)



def _sync_setup():
    async def _async_setup():
        async with engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
        yield
        async with engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.drop_all)

    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        gen = _async_setup()
        new_loop.run_until_complete(gen.__anext__())
        yield
        try:
            new_loop.run_until_complete(gen.__anext__())
        except StopAsyncIteration:
            pass
    finally:
        new_loop.close()
        asyncio.set_event_loop(None)

@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    yield from _sync_setup()

async def override_get_db():
    async with TestingSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
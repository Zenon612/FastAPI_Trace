from fastapi import APIRouter, Query, Depends
from app.schemas.health_schema import HealthCreate, HealthRead
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.health_model import HealthModel
from typing import Literal

router = APIRouter(prefix="/health")

@router.get("/", response_model=HealthCreate)
async def health(
        status: Literal["ok", "down"] = Query(default="ok", description="Статус"),
        message: str | None = Query(default=None, description="Доп сообщение"),
        db: AsyncSession = Depends(get_db),
):
        return {
                "status":status,
                "message":message,
                "timestamp" : datetime.now(),
        }

@router.post("/", response_model=HealthRead)
async def check_health(
        health_data: HealthCreate,
        db: AsyncSession = Depends(get_db)
):
        data = HealthModel(**health_data.model_dump())
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data
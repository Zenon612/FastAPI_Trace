from fastapi import APIRouter, Query, Depends
from app.schemas.health_schema import HealthSchema
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter(prefix="/health")

@router.get("/", response_model=HealthSchema)
async def health(
        status: str = Query(default="ok", description="Статус"),
        message: str | None = Query(default=None, description="Доп сообщение"),
        db: AsyncSession = Depends(get_db),
):
        return {
                "status":status,
                "message":message,
                "timestamp" : datetime.now(),
        }
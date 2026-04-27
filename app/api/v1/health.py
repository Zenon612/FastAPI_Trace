from fastapi import APIRouter, Query
from app.schemas.health_schema import HealthSchema
from datetime import datetime

router = APIRouter(prefix="/health")

@router.get("/", response_model=HealthSchema)
async def health(
        status: str = Query(default="ok", description="Статус"),
        message: str | None = Query(default=None, description="Доп сообщение")
):
        return {
                "status":status,
                "message":message,
                "timestamp" : datetime.now(),
        }
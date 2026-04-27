from fastapi import APIRouter
from app.schemas.health_schema import HealthSchema
from datetime import datetime

router = APIRouter(prefix="/health")
@router.get("/", response_model=HealthSchema)
async def health(status: str = "ok", time: datetime = datetime.now(), message: str | None = None):
        return {"status": status, "time": time, "message": message}
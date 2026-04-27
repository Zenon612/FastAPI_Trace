from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(prefix="/api/v1")

app.include_router(health_router, tags=["Health"])
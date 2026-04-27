from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.v1.health import router as health_router
import json

class UTF8Response(JSONResponse):
    def render(self, content) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            indent=2,
        ).encode("utf-8")


app = FastAPI(default_response_class=UTF8Response)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
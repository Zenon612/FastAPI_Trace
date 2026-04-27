from pydantic import BaseModel, Field
from datetime import datetime

class HealthSchema(BaseModel):
    status: str = Field(..., title="Статус")
    time: datetime = Field(default_factory= lambda: datetime.now())
    message: str | None = Field(default=None)
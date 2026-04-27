from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class HealthCreate(BaseModel):
    status: str = Field(..., title="Статус")
    message: str | None = Field(default=None)

class HealthRead(BaseModel):
    id: int
    status: str
    message: str | None
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
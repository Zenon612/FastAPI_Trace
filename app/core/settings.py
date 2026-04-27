from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    model_config_dict = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )
    app_name: str = Field(..., validation_alias="APP_NAME")
    app_version: int = Field(..., validation_alias="APP_VERSION")
    debug: bool = Field(default=True, validation_alias="DEBUG")
    database_url: str = Field(..., validation_alias="DATABASE_URL")
    secret_key: str = Field(..., validation_alias="SECRET_KEY")
    algorithm: str = Field(..., validation_alias="ALGORITHM")
settings = Settings()
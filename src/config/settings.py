from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str 

    auth_api_base: str = "http://talkxitauth:8001/api/v1"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

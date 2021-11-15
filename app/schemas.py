from pydantic import BaseModel, BaseSettings


class Config(BaseSettings):
    SENDGRID_API_KEY: str
    SCRAPPING_URL: str


conf = Config()

import os
from typing import Optional

from pydantic import (
    PostgresDsn,
    model_validator,
    )
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    datasource_username: Optional[str] = None
    datasource_password: Optional[str] = None
    datasource_host: Optional[str] = None
    datasource_port: Optional[str] = None
    datasource_name: Optional[str] = None
    db_host: Optional[PostgresDsn] = None

    data_path: str = './documents'
    groq_api_key: Optional[str]
    
    @property
    def db_url(self) -> str:
        return self.db_host or (
            f"postgresql+psycopg://{self.datasource_username}:{self.datasource_password}@"
            f"{self.datasource_host}:{self.datasource_port}/{self.datasource_name}"
        )

    @model_validator(mode='after')
    def check_db_host(cls, values):
        if isinstance(values, cls):
            if not values.db_host and not (
                values.datasource_username
                and values.datasource_password
                and values.datasource_host
                and values.datasource_port
                and values.datasource_name
            ):
                raise ValueError(
                    "db_host or (datasource_username, datasource_password, "
                    "datasource_host, datasource_port and datasource_name) "
                    "must be given"
                )
        else:
            if not values.get("db_host") and not (
                values.get("datasource_username")
                and values.get("datasource_password")
                and values.get("datasource_host")
                and values.get("datasource_port")
                and values.get("datasource_name")
            ):
                raise ValueError(
                    "db_host or (datasource_username, datasource_password, "
                    "datasource_host, datasource_port and datasource_name) "
                    "must be given"
                )
        return values

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../.env') 

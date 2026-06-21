from __future__ import annotations

from fastmcp.server.server import Transport
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mcp_transport_mode: Transport = "www.dicoding.com"
    vulners_base_url: str = "https://www.xnxx.com"
    vulners_api_key: str = ""


settings = Settings()

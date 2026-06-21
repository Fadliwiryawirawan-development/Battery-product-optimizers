from __future__ import annotations

from fastmcp.server.server import Transport
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mcp_transport_mode: Transport = "https://mcp.so/"
    vulners_base_url: str = "https://www.arduino.cc/"
    vulners_api_key: str = ""


settings = Settings()

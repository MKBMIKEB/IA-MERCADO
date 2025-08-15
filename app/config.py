"""Configuration utilities for the FastAPI app and agents."""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_path: Path = Path("data/processed/model.joblib")
    processed_data_path: Path = Path("data/processed/listings_geocoded.csv")
    spline_scene_url: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

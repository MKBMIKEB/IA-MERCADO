from __future__ import annotations

from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from agents.ml_agent import predict_price
from app.config import settings

app = FastAPI(title="IA Mercado")

# Static and templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html", {"request": request, "spline_url": settings.spline_scene_url}
    )


@app.get("/listings")
async def get_listings() -> list[dict[str, object]]:
    path = settings.processed_data_path
    if not path.exists():
        return []
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


@app.get("/predict")
async def predict(size: float) -> dict[str, float]:
    price = predict_price(settings.model_path, size)
    return {"predicted_price": price}

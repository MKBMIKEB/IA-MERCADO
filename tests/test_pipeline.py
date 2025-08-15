from __future__ import annotations

from pathlib import Path

import pandas as pd

from agents.ingest_agent import parse_listings_from_html
from agents.clean_agent import clean_listings
from agents.geocode_agent import geocode_listings
from agents.ml_agent import predict_price, train_price_model


def test_pipeline(tmp_path: Path) -> None:
    html = Path("tests/fixtures/sample.html").read_text()
    listings = parse_listings_from_html(html)
    df = pd.DataFrame(listings)
    raw = tmp_path / "raw.csv"
    df.to_csv(raw, index=False)

    clean = tmp_path / "clean.csv"
    clean_listings(raw, clean)

    def fake_geocode(address: str) -> tuple[float, float]:
        return 4.0, -74.0

    geo = tmp_path / "geo.csv"
    geocode_listings(clean, geo, geocode_fn=fake_geocode)

    model = tmp_path / "model.joblib"
    train_price_model(geo, model)

    pred = predict_price(model, 90.0)
    assert isinstance(pred, float)

"""Agent that trains simple machine learning models."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression


def train_price_model(csv_path: Path, model_path: Path) -> Path:
    df = pd.read_csv(csv_path).dropna(subset=["price", "size"])
    X = df[["size"]]
    y = df["price"]
    model = LinearRegression()
    model.fit(X, y)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    dump(model, model_path)
    return model_path


def predict_price(model_path: Path, size: float) -> float:
    model: LinearRegression = load(model_path)
    pred = model.predict([[size]])[0]
    return float(pred)

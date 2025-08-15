"""Agent for cleaning and normalising raw real estate data."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def clean_listings(csv_path: Path, output_path: Path) -> Path:
    """Clean and normalise listing information.

    - Normalises price and size to numeric values.
    - Title-cases addresses.
    - Removes duplicated listings.
    """

    df = pd.read_csv(csv_path)
    df["price"] = (
        df["price"].astype(str).str.replace(r"[^0-9.]", "", regex=True).astype(float)
    )
    df["size"] = (
        df["size"].astype(str).str.replace(r"[^0-9.]", "", regex=True).astype(float)
    )
    df["address"] = df["address"].astype(str).str.strip().str.title()
    df = df.drop_duplicates(subset=["title", "address"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

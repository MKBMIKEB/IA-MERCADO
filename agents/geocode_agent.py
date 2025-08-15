"""Agent that geocodes cleaned listings."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Tuple

import pandas as pd
from geopy.geocoders import Nominatim


GeoFunc = Callable[[str], Tuple[float, float] | Tuple[None, None]]


def default_geocode(address: str) -> Tuple[float, float] | Tuple[None, None]:
    geolocator = Nominatim(user_agent="ia_mercado")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None


def geocode_listings(
    csv_path: Path, output_path: Path, geocode_fn: GeoFunc | None = None
) -> Path:
    """Geocode addresses using the provided ``geocode_fn``.

    ``geocode_fn`` defaults to using :class:`geopy.geocoders.Nominatim` but can be
    replaced for testing purposes.
    """

    if geocode_fn is None:
        geocode_fn = default_geocode

    df = pd.read_csv(csv_path)
    latitudes = []
    longitudes = []
    for address in df["address"].astype(str):
        lat, lon = geocode_fn(address)
        latitudes.append(lat)
        longitudes.append(lon)
    df["latitude"] = latitudes
    df["longitude"] = longitudes
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

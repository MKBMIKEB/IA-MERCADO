"""Agent responsible for ingesting raw real estate data."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import requests
from bs4 import BeautifulSoup


def parse_listings_from_html(html: str) -> List[Dict[str, Any]]:
    """Parse a minimal HTML page and extract listing information.

    The function expects elements with the following structure::

        <div class="listing">
            <h2 class="title">Title</h2>
            <span class="price">$1000</span>
            <span class="address">Street 123</span>
            <span class="size">80 m2</span>
        </div>

    Parameters
    ----------
    html: str
        Raw HTML text.

    Returns
    -------
    list of dict
        Extracted listings.
    """

    soup = BeautifulSoup(html, "html.parser")
    listings: List[Dict[str, Any]] = []
    for node in soup.select("div.listing"):
        title = node.select_one("h2.title")
        price = node.select_one("span.price")
        address = node.select_one("span.address")
        size = node.select_one("span.size")
        if not (title and price and address and size):
            continue
        listings.append(
            {
                "title": title.text.strip(),
                "price": price.text.strip(),
                "address": address.text.strip(),
                "size": size.text.strip(),
            }
        )
    return listings


def ingest_page(url: str, output_path: Path) -> Path:
    """Download a web page and store parsed listings as CSV."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    listings = parse_listings_from_html(response.text)
    df = pd.DataFrame(listings)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

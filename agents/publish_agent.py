"""Agent that exposes the processed data and models via FastAPI."""

from __future__ import annotations

import uvicorn


def run() -> None:
    """Run the FastAPI application."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    run()

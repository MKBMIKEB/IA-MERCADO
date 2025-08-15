# IA Mercado

Sistema de mercados inmobiliarios basado en agentes inteligentes.

## Requisitos
- Python 3.11+
- Docker y docker-compose

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
```

## Ejecución local
```bash
uvicorn app.main:app --reload
```

O utilizando Docker:
```bash
./start.sh
```

## Pipeline de agentes
1. **Ingesta**: `agents/ingest_agent.py`
2. **Limpieza**: `agents/clean_agent.py`
3. **Geocodificación**: `agents/geocode_agent.py`
4. **Análisis y ML**: `agents/ml_agent.py`
5. **Publicación**: `agents/publish_agent.py`

## Variables de entorno
Ver `.env.example` para los valores configurables.

## Tests
```bash
python -m pytest
```

## Frontend
Aplicación React con Tailwind y Leaflet en `frontend/`.

## CI/CD
Workflow de GitHub Actions en `.github/workflows/ci.yml`.

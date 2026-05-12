# EV vs ICE Vehicle Analytics ETL

Dockerized batch ETL project for analyzing EV and ICE vehicle specifications from CSV data. The pipeline loads raw data into PostgreSQL using a Bronze -> Silver -> Gold layout and exposes analytics-ready Gold tables for Metabase dashboards.

## Stack

- Python ETL with pandas and SQLAlchemy
- PostgreSQL 16
- pgAdmin4
- Metabase
- Docker Compose

## Project Layout

```text
configs/vehicle_specs.yaml    Dataset config and table mappings
data/raw/                     Source CSV files
etl/                          Python ETL package
sql/                          Reference table schemas
docs/                         Architecture and dashboard notes
metabase/                     Metabase setup notes
```

## Run

Start PostgreSQL, pgAdmin, and Metabase:

```bash
docker compose up -d postgres pgadmin metabase
```

Run the full ETL:

```bash
docker compose run --rm etl python -m etl.main --pipeline all
```

Run one layer:

```bash
docker compose run --rm etl python -m etl.main --pipeline bronze
docker compose run --rm etl python -m etl.main --pipeline silver
docker compose run --rm etl python -m etl.main --pipeline gold
```

## Services

- PostgreSQL: `localhost:5433` by default, or `POSTGRES_HOST_PORT` if set
- pgAdmin: `http://localhost:5050`
- Metabase: `http://localhost:3000`

Default local credentials are in `.env`.

## Tables

Bronze:

- `bronze_vehicle_specs`

Silver:

- `silver_vehicle_specs`

Gold:

- `gold_vehicle_count_by_year_fuel_type`
- `gold_avg_efficiency_by_fuel_type`
- `gold_avg_co2_by_category`
- `gold_top_makes_by_ev_count`
- `gold_avg_ev_range_by_year`

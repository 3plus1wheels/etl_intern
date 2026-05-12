# Metabase Setup

Start Metabase with:

```bash
docker compose up -d metabase
```

Connect Metabase to PostgreSQL using these settings from inside the Docker network:

- Host: `postgres`
- Port: `5432`
- Database: `vehicle_analytics`
- Username: `postgres`
- Password: use the current `POSTGRES_PASSWORD` value from `.env`

Use the Gold tables as dashboard sources:

- `gold_vehicle_count_by_year_fuel_type`
- `gold_avg_efficiency_by_fuel_type`
- `gold_avg_co2_by_category`
- `gold_top_makes_by_ev_count`
- `gold_avg_ev_range_by_year`

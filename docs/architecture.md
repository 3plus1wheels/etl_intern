# Architecture

The project uses a batch ETL architecture:

```text
CSV files -> Bronze -> Silver -> Gold -> Metabase
```

## Bronze

`bronze_vehicle_specs` stores source CSV rows with minimal changes. The pipeline appends metadata columns:

- `ingested_at`
- `source_file`
- `batch_id`

## Silver

`silver_vehicle_specs` stores cleaned and enriched vehicle records. It standardizes column names, converts data types, normalizes missing fuel types, renames MPG fields to efficiency fields, and adds EV/ICE classification and validation flags.

## Gold

Gold tables are dashboard-ready aggregations for count trends, EV range, emissions, efficiency, and top EV manufacturers.

## Configuration

Dataset-specific paths, table names, column types, renames, and validation bounds are kept in `configs/vehicle_specs.yaml`.

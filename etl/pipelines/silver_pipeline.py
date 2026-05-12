from etl.load.postgres_loader import read_table_from_postgres, load_dataframe_to_postgres
from etl.transform.cleaning import clean_column_names, rename_efficiency_columns, standardize_text_fields
from etl.transform.validation import add_validation_flags
from etl.transform.vehicle_rules import add_vehicle_derived_columns, convert_vehicle_types
from etl.utils.logger import get_logger

logger = get_logger(__name__)


def run(config: dict, engine) -> None:
    bronze_table = config["bronze_table"]
    silver_table = config["silver_table"]

    df = read_table_from_postgres(bronze_table, engine)
    df = clean_column_names(df)
    df = rename_efficiency_columns(df, config.get("column_renames", {}))
    df = standardize_text_fields(df)
    df = convert_vehicle_types(df)
    df = add_vehicle_derived_columns(df)
    df = add_validation_flags(df, config)

    load_dataframe_to_postgres(df, silver_table, engine)
    logger.info("Loaded %s rows into %s", len(df), silver_table)

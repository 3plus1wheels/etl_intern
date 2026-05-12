from etl.load.postgres_loader import load_dataframe_to_postgres, read_table_from_postgres
from etl.transform.aggregations import create_gold_tables
from etl.utils.logger import get_logger

logger = get_logger(__name__)


def run(config: dict, engine) -> None:
    silver = read_table_from_postgres(config["silver_table"], engine)
    gold_frames = create_gold_tables(silver)

    configured_names = config["gold_tables"]
    for logical_name, df in gold_frames.items():
        table_name = configured_names[logical_name]
        load_dataframe_to_postgres(df, table_name, engine)
        logger.info("Loaded %s rows into %s", len(df), table_name)

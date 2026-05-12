from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from etl.extract.csv_loader import load_csv
from etl.load.postgres_loader import load_dataframe_to_postgres
from etl.utils.logger import get_logger

logger = get_logger(__name__)


def run(config: dict, engine) -> None:
    source_file = Path(config["source_file"])
    df = load_csv(source_file)

    batch_id = str(uuid4())
    df["ingested_at"] = datetime.now(UTC)
    df["source_file"] = str(source_file)
    df["batch_id"] = batch_id

    table_name = config["bronze_table"]
    load_dataframe_to_postgres(df, table_name, engine)
    logger.info("Loaded %s rows into %s with batch_id=%s", len(df), table_name, batch_id)

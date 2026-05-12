import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine


def load_dataframe_to_postgres(
    df: pd.DataFrame,
    table_name: str,
    engine: Engine,
    if_exists: str = "replace",
) -> None:
    df.to_sql(table_name, engine, if_exists=if_exists, index=False, method="multi", chunksize=1000)


def read_table_from_postgres(table_name: str, engine: Engine) -> pd.DataFrame:
    return pd.read_sql_table(table_name, engine)


def table_exists(table_name: str, engine: Engine) -> bool:
    query = text(
        """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_name = :table_name
        )
        """
    )
    with engine.connect() as conn:
        return bool(conn.execute(query, {"table_name": table_name}).scalar())

import argparse

from etl.pipelines import bronze_pipeline, gold_pipeline, silver_pipeline
from etl.utils.config_reader import load_config
from etl.utils.db import get_engine
from etl.utils.logger import get_logger

logger = get_logger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the vehicle analytics ETL pipeline.")
    parser.add_argument(
        "--pipeline",
        choices=["bronze", "silver", "gold", "all"],
        default="all",
        help="Pipeline stage to run.",
    )
    parser.add_argument(
        "--config",
        default="configs/vehicle_specs.yaml",
        help="Path to the dataset config file.",
    )
    return parser.parse_args()


def run_pipeline(pipeline: str, config_path: str) -> None:
    config = load_config(config_path)
    engine = get_engine()

    if pipeline in {"bronze", "all"}:
        logger.info("Starting Bronze pipeline")
        bronze_pipeline.run(config, engine)

    if pipeline in {"silver", "all"}:
        logger.info("Starting Silver pipeline")
        silver_pipeline.run(config, engine)

    if pipeline in {"gold", "all"}:
        logger.info("Starting Gold pipeline")
        gold_pipeline.run(config, engine)

    logger.info("Pipeline complete: %s", pipeline)


def main() -> None:
    args = parse_args()
    run_pipeline(args.pipeline, args.config)


if __name__ == "__main__":
    main()

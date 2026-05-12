from pathlib import Path

import pandas as pd


def load_csv(source_file: str | Path) -> pd.DataFrame:
    path = Path(source_file)
    if not path.exists():
        raise FileNotFoundError(f"CSV source file not found: {path}")
    return pd.read_csv(path)

import re

import pandas as pd


def to_snake_case(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z]+", "_", value.strip())
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.strip("_").lower()


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result.columns = [to_snake_case(column) for column in result.columns]
    return result


def rename_efficiency_columns(df: pd.DataFrame, renames: dict[str, str]) -> pd.DataFrame:
    return df.rename(columns=renames)


def standardize_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for column in result.select_dtypes(include=["object"]).columns:
        result[column] = result[column].astype("string").str.strip()

    if "fuel_type" in result.columns:
        result["fuel_type"] = result["fuel_type"].fillna("Unknown")
        result.loc[result["fuel_type"].str.len().fillna(0).eq(0), "fuel_type"] = "Unknown"

    return result

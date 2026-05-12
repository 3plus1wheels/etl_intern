import pandas as pd


def add_validation_flags(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    result = df.copy()
    validations = config.get("validations", {})
    year_min = validations.get("year_min")
    year_max = validations.get("year_max")
    required_columns = config.get("required_columns", [])

    result["is_valid_year"] = result["year"].between(year_min, year_max, inclusive="both")

    result["is_valid_ev_range"] = (~result["is_ev"]) | (result["ev_range_miles"].fillna(0) > 0)
    result["is_valid_engine_for_ev"] = (
        (~result["is_ev"])
        | (
            result["engine_cylinders"].fillna(-1).eq(0)
            & result["engine_size_l"].fillna(-1).eq(0)
        )
    )
    result["is_valid_emissions_for_ev"] = (
        (~result["is_ev"]) | result["co2_emissions_g_per_mile"].fillna(-1).eq(0)
    )

    missing_required = pd.Series(False, index=result.index)
    for column in required_columns:
        if column not in result.columns:
            missing_required = True
            continue
        values = result[column]
        missing_required = missing_required | values.isna()
        if pd.api.types.is_string_dtype(values) or values.dtype == object:
            missing_required = missing_required | values.astype("string").str.strip().eq("")

    result["has_missing_required_fields"] = missing_required

    if {"city_efficiency", "highway_efficiency", "combined_efficiency"}.issubset(result.columns):
        lower = result[["city_efficiency", "highway_efficiency"]].min(axis=1)
        upper = result[["city_efficiency", "highway_efficiency"]].max(axis=1)
        result["is_valid_combined_efficiency"] = result["combined_efficiency"].between(lower, upper)

    return result

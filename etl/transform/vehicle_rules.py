import pandas as pd


NUMERIC_COLUMNS = [
    "year",
    "engine_cylinders",
    "engine_size_l",
    "city_efficiency",
    "highway_efficiency",
    "combined_efficiency",
    "co2_emissions_g_per_mile",
    "ev_range_miles",
]


INTEGER_COLUMNS = ["year", "engine_cylinders"]


def convert_vehicle_types(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    for column in NUMERIC_COLUMNS:
        if column in result.columns:
            result[column] = pd.to_numeric(result[column], errors="coerce")

    for column in INTEGER_COLUMNS:
        if column in result.columns:
            result[column] = result[column].astype("Int64")

    return result


def add_vehicle_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    fuel = result["fuel_type"].fillna("Unknown").astype("string").str.lower()

    result["is_ev"] = fuel.str.contains("electric|electricity|ev", regex=True, na=False)
    result["is_ice"] = fuel.str.contains("gasoline|diesel", regex=True, na=False) & ~result["is_ev"]
    result["is_hybrid_or_other"] = ~(result["is_ev"] | result["is_ice"])
    result["efficiency_unit"] = result["is_ev"].map({True: "MPGe", False: "MPG"})

    return result

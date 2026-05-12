import pandas as pd


def create_vehicle_count_by_year_fuel_type(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["year", "fuel_type"], dropna=False)
        .size()
        .reset_index(name="vehicle_count")
        .sort_values(["year", "fuel_type"])
    )


def create_avg_efficiency_by_fuel_type(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["fuel_type", "efficiency_unit"], dropna=False)
        .agg(
            avg_city_efficiency=("city_efficiency", "mean"),
            avg_highway_efficiency=("highway_efficiency", "mean"),
            avg_combined_efficiency=("combined_efficiency", "mean"),
            vehicle_count=("model", "count"),
        )
        .reset_index()
        .sort_values(["fuel_type", "efficiency_unit"])
    )


def create_avg_co2_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["vehicle_category", "fuel_type"], dropna=False)
        .agg(
            avg_co2_emissions_g_per_mile=("co2_emissions_g_per_mile", "mean"),
            vehicle_count=("model", "count"),
        )
        .reset_index()
        .sort_values(["vehicle_category", "fuel_type"])
    )


def create_top_makes_by_ev_count(df: pd.DataFrame, limit: int = 15) -> pd.DataFrame:
    ev = df[df["is_ev"]].copy()
    return (
        ev.groupby("make", dropna=False)
        .agg(
            ev_count=("model", "count"),
            avg_ev_range_miles=("ev_range_miles", "mean"),
            avg_combined_efficiency=("combined_efficiency", "mean"),
        )
        .reset_index()
        .sort_values(["ev_count", "avg_ev_range_miles"], ascending=[False, False])
        .head(limit)
    )


def create_avg_ev_range_by_year(df: pd.DataFrame) -> pd.DataFrame:
    ev = df[df["is_ev"]].copy()
    return (
        ev.groupby("year", dropna=False)
        .agg(
            avg_ev_range_miles=("ev_range_miles", "mean"),
            min_ev_range_miles=("ev_range_miles", "min"),
            max_ev_range_miles=("ev_range_miles", "max"),
            ev_count=("model", "count"),
        )
        .reset_index()
        .sort_values("year")
    )


def create_gold_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        "vehicle_count_by_year_fuel_type": create_vehicle_count_by_year_fuel_type(df),
        "avg_efficiency_by_fuel_type": create_avg_efficiency_by_fuel_type(df),
        "avg_co2_by_category": create_avg_co2_by_category(df),
        "top_makes_by_ev_count": create_top_makes_by_ev_count(df),
        "avg_ev_range_by_year": create_avg_ev_range_by_year(df),
    }

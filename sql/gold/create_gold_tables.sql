CREATE TABLE IF NOT EXISTS gold_vehicle_count_by_year_fuel_type (
    year integer,
    fuel_type text,
    vehicle_count bigint
);

CREATE TABLE IF NOT EXISTS gold_avg_efficiency_by_fuel_type (
    fuel_type text,
    efficiency_unit text,
    avg_city_efficiency double precision,
    avg_highway_efficiency double precision,
    avg_combined_efficiency double precision,
    vehicle_count bigint
);

CREATE TABLE IF NOT EXISTS gold_avg_co2_by_category (
    vehicle_category text,
    fuel_type text,
    avg_co2_emissions_g_per_mile double precision,
    vehicle_count bigint
);

CREATE TABLE IF NOT EXISTS gold_top_makes_by_ev_count (
    make text,
    ev_count bigint,
    avg_ev_range_miles double precision,
    avg_combined_efficiency double precision
);

CREATE TABLE IF NOT EXISTS gold_avg_ev_range_by_year (
    year integer,
    avg_ev_range_miles double precision,
    min_ev_range_miles double precision,
    max_ev_range_miles double precision,
    ev_count bigint
);

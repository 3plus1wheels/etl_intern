CREATE TABLE IF NOT EXISTS bronze_vehicle_specs (
    "Make" text,
    "Model" text,
    "Year" integer,
    "Fuel_Type" text,
    "Engine_Cylinders" double precision,
    "Engine_Size_L" double precision,
    "Drivetrain" text,
    "Transmission" text,
    "City_MPG" double precision,
    "Highway_MPG" double precision,
    "Combined_MPG" double precision,
    "CO2_Emissions_g_per_mile" double precision,
    "EV_Range_miles" double precision,
    "Vehicle_Category" text,
    ingested_at timestamptz,
    source_file text,
    batch_id text
);

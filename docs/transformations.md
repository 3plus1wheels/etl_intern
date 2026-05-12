# Transformations

## Column Cleaning

Source columns are converted to snake case. Efficiency columns are renamed:

- `City_MPG` -> `city_efficiency`
- `Highway_MPG` -> `highway_efficiency`
- `Combined_MPG` -> `combined_efficiency`

## Type Conversion

Numeric vehicle fields are converted with invalid values preserved as nulls:

- `year`
- `engine_cylinders`
- `engine_size_l`
- `city_efficiency`
- `highway_efficiency`
- `combined_efficiency`
- `co2_emissions_g_per_mile`
- `ev_range_miles`

## Vehicle Rules

Rows are classified with:

- `is_ev`
- `is_ice`
- `is_hybrid_or_other`
- `efficiency_unit`

EV efficiency values use `MPGe`; non-EV values use `MPG`.

## Validation Flags

Rows are not dropped for quality issues. The Silver layer adds flags:

- `is_valid_year`
- `is_valid_ev_range`
- `is_valid_engine_for_ev`
- `is_valid_emissions_for_ev`
- `has_missing_required_fields`
- `is_valid_combined_efficiency`

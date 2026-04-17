import pandas as pd
import os

# Load data
df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

# Create output folder
os.makedirs("data/warehouse", exist_ok=True)

# ==============================
# DIMENSION: LOCATION
# ==============================
dim_location = df[["location"]].drop_duplicates().reset_index(drop=True)
dim_location["location_id"] = dim_location.index + 1

# ==============================
# DIMENSION: WEATHER
# ==============================
dim_weather = df[["weather"]].drop_duplicates().reset_index(drop=True)
dim_weather["weather_id"] = dim_weather.index + 1

# ==============================
# DIMENSION: TIME
# ==============================
dim_time = df[["hour", "day"]].drop_duplicates().reset_index(drop=True)
dim_time["time_id"] = dim_time.index + 1

# ==============================
# MAP IDS BACK TO FACT TABLE
# ==============================
df = df.merge(dim_location, on="location")
df = df.merge(dim_weather, on="weather")
df = df.merge(dim_time, on=["hour", "day"])

# ==============================
# FACT TABLE
# ==============================
fact_traffic = df[[
    "location_id",
    "weather_id",
    "time_id",
    "vehicle_count",
    "avg_speed",
    "accident",
    "congestion",
    "traffic_level"
]]

# ==============================
# SAVE CSVs
# ==============================
dim_location.to_csv("data/warehouse/dim_location.csv", index=False)
dim_weather.to_csv("data/warehouse/dim_weather.csv", index=False)
dim_time.to_csv("data/warehouse/dim_time.csv", index=False)
fact_traffic.to_csv("data/warehouse/fact_traffic.csv", index=False)

print("✅ Snowflake schema CSVs created!")
import pandas as pd

# Load data
df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -----------------------------
# DIMENSION TABLES
# -----------------------------

# Location dimension
dim_location = df[['location']].drop_duplicates().reset_index(drop=True)
dim_location['location_id'] = dim_location.index + 1

# Time dimension
dim_time = df[['timestamp']].drop_duplicates().reset_index(drop=True)
dim_time['time_id'] = dim_time.index + 1
dim_time['hour'] = dim_time['timestamp'].dt.hour
dim_time['day'] = dim_time['timestamp'].dt.day
dim_time['month'] = dim_time['timestamp'].dt.month

# -----------------------------
# FACT TABLE
# -----------------------------

# Merge IDs
df = df.merge(dim_location, on='location')
df = df.merge(dim_time, on='timestamp')

fact_traffic = df[['location_id', 'time_id', 'vehicle_count', 'avg_speed']]

# -----------------------------
# SAVE FILES
# -----------------------------

dim_location.to_csv("data/star/dim_location.csv", index=False)
dim_time.to_csv("data/star/dim_time.csv", index=False)
fact_traffic.to_csv("data/star/fact_traffic.csv", index=False)

print("✅ Star schema created successfully!")
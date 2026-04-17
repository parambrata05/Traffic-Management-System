import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="traffic_user",
    password="password123",
    database="traffic_db"
)
cursor = conn.cursor()

# 🔹 Load CSV
df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

# 🔹 Map location → location_id
location_map = {
    "Junction_A": 1,
    "Junction_B": 2,
    "Junction_C": 3,
    "Junction_D": 4
}

df["location_id"] = df["location"].map(location_map)

# 🔹 Insert row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO traffic_data (
            timestamp, location_id, vehicle_count, avg_speed,
            weather, accident, congestion, hour, day, traffic_level
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["timestamp"],
        row["location_id"],
        row["vehicle_count"],
        row["avg_speed"],
        row["weather"],
        row["accident"],
        row["congestion"],
        row["hour"],
        row["day"],
        row["traffic_level"]
    ))

# 🔹 Commit + close
conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted into MySQL!")
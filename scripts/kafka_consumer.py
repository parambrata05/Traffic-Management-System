from kafka import KafkaConsumer
import json
import mysql.connector

# Location mapping
location_map = {
    "Junction_A": 1,
    "Junction_B": 2,
    "Junction_C": 3,
    "Junction_D": 4
}

consumer = KafkaConsumer(
    'traffic-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = mysql.connector.connect(
    host="localhost",
    user="traffic_user",
    password="password123",
    database="traffic_db"
)

cursor = conn.cursor()

print("📥 Consumer started...")

for message in consumer:
    data = message.value

    location_id = location_map[data["location"]]

    cursor.execute("""
        INSERT INTO traffic_data (
            timestamp, location_id, vehicle_count, avg_speed,
            weather, accident, congestion, hour, day, traffic_level
        )
        VALUES (NOW(), %s, %s, %s, %s, 0, 0, %s, 'Live', 'Medium')
    """, (
        location_id,
        data["vehicle_count"],
        data["avg_speed"],
        data["weather"],
        data["hour"]
    ))

    conn.commit()
    print("Inserted:", data)
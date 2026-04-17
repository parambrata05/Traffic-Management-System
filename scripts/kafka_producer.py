from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

locations = ["Junction_A", "Junction_B", "Junction_C", "Junction_D"]

print("🚀 Producer started...")

while True:
    data = {
        "location": random.choice(locations),
        "vehicle_count": random.randint(10, 100),
        "avg_speed": round(random.uniform(10, 80), 2),
        "weather": random.randint(0, 2),
        "hour": random.randint(0, 23)
    }

    producer.send('traffic-data', value=data)
    print("Sent:", data)

    time.sleep(2)
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_traffic_data(n=5000):
    data = []

    locations = ["Junction_A", "Junction_B", "Junction_C", "Junction_D"]
    weather_conditions = ["Clear", "Rain", "Fog"]

    start_time = datetime.now() - timedelta(days=1)

    for _ in range(n):
        timestamp = start_time + timedelta(minutes=random.randint(0, 1440))
        location = random.choice(locations)

        # Peak hour logic
        hour = timestamp.hour
        if 8 <= hour <= 11 or 17 <= hour <= 20:
            vehicle_count = random.randint(60, 120)
            avg_speed = random.uniform(10, 40)
        else:
            vehicle_count = random.randint(10, 60)
            avg_speed = random.uniform(30, 80)

        weather = random.choice(weather_conditions)
        accident = 1 if random.random() < 0.05 else 0

        congestion = int(vehicle_count > 80 or avg_speed < 20 or accident == 1)

        data.append({
            "timestamp": timestamp,
            "location": location,
            "vehicle_count": vehicle_count,
            "avg_speed": round(avg_speed, 2),
            "weather": weather,
            "accident": accident,
            "congestion": congestion
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_traffic_data()
    df.to_csv("data/raw/traffic_data.csv", index=False)
    print("✅ Data generated successfully!")
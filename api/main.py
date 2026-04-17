from fastapi import FastAPI
import joblib
import pandas as pd
import mysql.connector

app = FastAPI(title="Smart Traffic Management API")

# ==============================
# LOAD ML MODEL
# ==============================
model = joblib.load("ml/traffic_model.pkl")

# ==============================
# DATABASE CONNECTION
# ==============================
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="traffic_user",
        password="password123",
        database="traffic_db"
    )

# ==============================
# ROOT ENDPOINT
# ==============================
@app.get("/")
def home():
    return {"message": "🚦 Smart Traffic API is running"}

# ==============================
# FETCH TRAFFIC DATA
# ==============================
@app.get("/traffic")
def get_traffic():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT t.id, l.location_name, t.vehicle_count, t.avg_speed,
           t.weather, t.congestion, t.hour
    FROM traffic_data t
    JOIN locations l ON t.location_id = l.location_id
    LIMIT 50;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

# ==============================
# PREDICT CONGESTION
# ==============================
@app.get("/predict")
def predict(vehicle_count: int, avg_speed: float, weather: int, hour: int):
    input_data = pd.DataFrame([{
        "vehicle_count": vehicle_count,
        "avg_speed": avg_speed,
        "weather": weather,
        "hour": hour
    }])

    prediction = model.predict(input_data)[0]

    return {
        "input": {
            "vehicle_count": vehicle_count,
            "avg_speed": avg_speed,
            "weather": weather,
            "hour": hour
        },
        "congestion_prediction": int(prediction)
    }

# ==============================
# GET STATISTICS
# ==============================
@app.get("/stats")
def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT l.location_name, AVG(t.vehicle_count) AS avg_traffic
    FROM traffic_data t
    JOIN locations l ON t.location_id = l.location_id
    GROUP BY l.location_name
    ORDER BY avg_traffic DESC;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
import pandas as pd

def check_data():
    df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

    print("---- Missing Values ----")
    print(df.isnull().sum())

    print("\n---- Data Summary ----")
    print(df.describe())

    # Anomaly detection
    anomalies = df[df["vehicle_count"] > 150]
    print(f"\nAnomalies found: {len(anomalies)}")

if __name__ == "__main__":
    check_data()
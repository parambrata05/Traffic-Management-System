import pandas as pd

def clean_data(df):
    df.fillna({
        "vehicle_count": 0,
        "avg_speed": df["avg_speed"].mean(),
        "weather": "Clear",
        "accident": 0
    }, inplace=True)
    return df


def transform_data(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.day_name()

    df["traffic_level"] = df["vehicle_count"].apply(
        lambda x: "High" if x > 80 else ("Medium" if x > 40 else "Low")
    )

    return df


def run_etl():
    df = pd.read_csv("data/raw/traffic_data.csv")

    df = clean_data(df)
    df = transform_data(df)

    df.to_csv("data/processed/traffic_data_cleaned.csv", index=False)

    print("✅ ETL completed!")


if __name__ == "__main__":
    run_etl()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

# Encode categorical data
le_weather = LabelEncoder()
df["weather"] = le_weather.fit_transform(df["weather"])

# Features and target
X = df[["vehicle_count", "avg_speed", "weather", "hour"]]
y = df["congestion"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc:.2f}")

# Save model
joblib.dump(model, "ml/traffic_model.pkl")
print("✅ Model saved!")
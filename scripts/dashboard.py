import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Traffic Dashboard", layout="wide")

st.title("🚦 Smart Traffic Dashboard")

# Load data
df = pd.read_csv("data/processed/traffic_data_cleaned.csv")

# Convert timestamp
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour

# Sidebar filter
st.sidebar.header("Filters")
locations = st.sidebar.multiselect(
    "Select Location",
    options=df['location'].unique(),
    default=df['location'].unique()
)

filtered_df = df[df['location'].isin(locations)]

# -----------------------------
# Traffic by Location
# -----------------------------
st.subheader("📊 Traffic by Location")

traffic_data = filtered_df.groupby('location')['vehicle_count'].mean()

fig1, ax1 = plt.subplots()
traffic_data.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Vehicle Count")
ax1.set_xlabel("Location")

st.pyplot(fig1)

# -----------------------------
# Speed Trend
# -----------------------------
if 'hour' in filtered_df.columns:
    st.subheader("🚗 Speed Trend")

    speed_data = filtered_df.groupby('hour')['avg_speed'].mean()

    fig2, ax2 = plt.subplots()
    speed_data.plot(ax=ax2)
    ax2.set_ylabel("Speed")
    ax2.set_xlabel("Hour")

    st.pyplot(fig2)

# -----------------------------
# Vehicle Distribution
# -----------------------------
st.subheader("📈 Vehicle Count Distribution")

fig3, ax3 = plt.subplots()
filtered_df['vehicle_count'].hist(bins=20, ax=ax3)

st.pyplot(fig3)

# -----------------------------
# Raw Data
# -----------------------------
st.subheader("📄 Raw Data Preview")
st.dataframe(filtered_df.head())
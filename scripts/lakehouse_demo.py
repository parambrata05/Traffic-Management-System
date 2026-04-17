from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Lakehouse Demo") \
    .getOrCreate()

# Load raw data
df = spark.read.csv(
    "data/processed/traffic_data_cleaned.csv",
    header=True,
    inferSchema=True
)

print("📥 Raw Data")
df.show(5)

# Save as Parquet (lakehouse storage)
df.write.mode("overwrite").parquet("data/lakehouse/traffic_parquet")

print("✅ Data stored in lakehouse format (Parquet)")

# Read back (like table)
df_parquet = spark.read.parquet("data/lakehouse/traffic_parquet")

print("📊 Querying Lakehouse Data")

df_parquet.groupBy("location").avg("vehicle_count").show()

spark.stop()
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# ==============================
# TASK 14: SPARK BASICS
# ==============================
spark = SparkSession.builder \
    .appName("Smart Traffic Spark Pipeline") \
    .getOrCreate()

print("✅ Spark Session Created")

# ==============================
# LOAD DATA
# ==============================
df = spark.read.csv(
    "data/processed/traffic_data_cleaned.csv",
    header=True,
    inferSchema=True
)

df.show(5)
df.printSchema()

# ==============================
# TASK 15: DATAFRAME OPERATIONS
# ==============================

# Filter high traffic
high_traffic = df.filter(df["vehicle_count"] > 50)

# Group by location
traffic_by_location = df.groupBy("location").agg(
    avg("vehicle_count").alias("avg_vehicles"),
    count("*").alias("records")
)

print("📊 Traffic by location:")
traffic_by_location.show()

# ==============================
# TASK 16: SPARK SQL
# ==============================

# Register temp table
df.createOrReplaceTempView("traffic")

sql_result = spark.sql("""
    SELECT location, AVG(vehicle_count) AS avg_traffic
    FROM traffic
    GROUP BY location
    ORDER BY avg_traffic DESC
""")

print("📈 Spark SQL Result:")
sql_result.show()

# ==============================
# TASK 17: ADVANCED PYSPARK
# ==============================

# Repartition data (parallelism)
df_repartitioned = df.repartition(4)

# Cache data (optimization)
df_repartitioned.cache()

print("⚡ Cached Data Count:", df_repartitioned.count())

# Write output
traffic_by_location.write.mode("overwrite").csv("data/spark_output")

print("✅ Spark job completed successfully")

# Stop session
spark.stop()
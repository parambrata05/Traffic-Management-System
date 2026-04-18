# 🚦 Smart Traffic Management System (Data Engineering Pipeline)

---

## 📌 Overview

This project implements a scalable end-to-end data engineering pipeline for traffic data. It covers the complete lifecycle from data ingestion to visualization using modern tools such as Kafka, Spark, Airflow, Hadoop, and AWS.

The system integrates real-time streaming, batch processing, distributed storage, and cloud deployment to simulate a real-world traffic analytics platform.

---

## 🧠 Problem Statement

Urban traffic systems generate large volumes of data across multiple locations and time intervals. However:

* Data exists in raw and unstructured formats
* No real-time streaming system
* Lack of centralized processing pipeline
* Difficult to analyze large-scale traffic patterns
* No interactive visualization for insights

---

## 💡 Solution

An end-to-end pipeline was built to:

* Generate and ingest traffic data
* Perform validation and transformation
* Store structured data in databases
* Process large datasets using Spark
* Simulate real-time streaming using Kafka
* Store data in HDFS and AWS S3
* Deploy compute using EC2
* Visualize insights using Streamlit dashboard

---

## 🏗️ Project Structure

```id="ps1"
smart-traffic-system/
│
├── api/                     # FastAPI backend
│   ├── main.py
├── data/                    #all the csv and parquet files
├── db/                      # SQL schema and queries
│   ├── insert.sql
│   ├── queries.sql
│    ├── query_output.txt
│   ├── schema.sql
├── ml/                      # Model training scripts
│   ├── train_model.py
├── scripts/                 # ETL, Kafka, Spark, Lakehouse scripts
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── spark_full_pipeline.py
│   ├── star_schema.py
│   ├── lakehouse_demo.py
│   ├── dashboard.py
│   ├──etl.py
│   ├──load_to_db.py
│   ├──quality_checks.py
│   ├──generate_data.py
│   ├── visualize.ipynb
│
├── README.md
└── .gitignore
```

---

## ⚙️ Features

### 🔹 1. Data Ingestion

* Synthetic traffic data generation
* FastAPI-based API endpoint

### 🔹 2. Streaming (Kafka)

* Producer sends real-time traffic data
* Consumer processes and stores data

### 🔹 3. Data Validation & Transformation

* Cleaning missing/null values
* Feature engineering
* Structured dataset creation

### 🔹 4. Workflow Orchestration (Airflow)

* DAG automates ETL pipeline
* Tasks include ingestion → processing → storage

### 🔹 5. Database Integration

* MySQL used for structured storage
* SQL queries for analytics

### 🔹 6. Big Data Processing (PySpark)

* DataFrame operations
* Spark SQL queries
* Partitioning and caching

### 🔹 7. Hadoop HDFS

* Distributed storage of processed data
* NameNode & DataNode configured

### 🔹 8. Lakehouse Simulation

* Data stored in Parquet format
* Queried using Spark
* Mimics Delta Lake / Iceberg architecture

### 🔹 9. Cloud Integration

* AWS S3 → data storage
* AWS EC2 → compute deployment

### 🔹 10. Dashboard (Streamlit)

Interactive dashboard provides:

* Traffic by location
* Speed trends
* Vehicle count distribution
* Filters for dynamic analysis

---

## 📊 Tech Stack

| Category      | Tools              |
| ------------- | ------------------ |
| Language      | Python             |
| Streaming     | Apache Kafka       |
| Processing    | Apache Spark       |
| Orchestration | Apache Airflow     |
| Storage       | MySQL, Hadoop HDFS |
| Cloud         | AWS S3, EC2        |
| Visualization | Streamlit          |

---

## 🚀 Unique Points

* End-to-end pipeline (Streaming + Batch + Cloud)
* Real-time + batch processing integration
* Distributed storage using Hadoop
* Lakehouse-style architecture using Spark
* Cloud deployment on AWS
* Interactive dashboard for insights

---

## 🔮 Future Improvements

* Real-time Spark Streaming integration
* Deployment of dashboard on cloud
* Integration with BigQuery/Redshift
* ML-based traffic prediction
* Alert system for congestion detection

---

## ▶️ How to Run

```id="run1"
# Activate environment
source venv/bin/activate

# Run data generation
python scripts/generate_data.py

# Run Kafka producer & consumer
python scripts/kafka_producer.py
python scripts/kafka_consumer.py

# Run Spark pipeline
python scripts/spark_full_pipeline.py

# Run dashboard
streamlit run dashboard.py
```

---

## 📊 Output

* Processed traffic dataset
* Aggregated analytics using Spark
* Interactive dashboard visualization

---

## 👨‍💻 Author

**Parambrata Acharjee**
B.Tech CSE | Data Engineering & ML Enthusiast

---

## 🧠 Key Learning

This project demonstrates building a complete modern data pipeline integrating streaming, batch processing, distributed systems, and cloud technologies.

---

## ⚠️ Note

Large files (datasets, Hadoop, Kafka binaries) are excluded using `.gitignore`.

---

## 🏁 Conclusion

This project showcases a real-world scalable data engineering architecture capable of handling large traffic datasets, ensuring data quality, and generating actionable insights.

---

# Real-Time Customer Analytics Platform

A production-style data engineering portfolio project that demonstrates real-time event streaming concepts, Databricks Delta Lake medallion architecture, and Airflow orchestration.

## Current Project Status

Implemented so far:

- Kafka running locally in **KRaft mode** using Docker Compose
- Python producer generating customer activity events
- Kafka topic `customer_events` with 3 partitions
- Python consumers using the same consumer group to validate offset tracking and rebalancing
- Databricks Bronze, Silver, and Gold Delta layers
- Airflow DAG skeleton to orchestrate Databricks notebooks

Terraform will be added next.

---

## Architecture

```text
Python Event Producer
        ↓
Kafka Topic: customer_events
        ↓
Consumer Group / Offset Tracking / Rebalancing
        ↓
Raw JSON Landing Zone
        ↓
Databricks Bronze Delta Layer
        ↓
Databricks Silver Delta Layer
        ↓
Databricks Gold Delta Layer
        ↑
Airflow DAG Orchestration
```

---

## Tech Stack

- Apache Kafka in KRaft mode
- Docker Compose
- Python
- Databricks
- Apache Spark / PySpark
- Structured Streaming
- Delta Lake
- Unity Catalog Volumes
- Airflow
- Terraform, planned next

---

## Repository Structure

```text
real-time-customer-analytics-platform/
│
├── kafka/
│   ├── producer/
│   ├── consumer/
│   ├── schemas/
│   └── topics/
│
├── databricks/
│   └── notebooks/
│       ├── bronze/
│       ├── silver/
│       ├── gold/
│       └── utilities/
│
├── airflow/
│   └── dags/
│
├── infrastructure/
│   └── docker/
│
├── docs/
│
└── requirements.txt
```

---

## Day 1 - Kafka Foundation

### Objective

Build a working Kafka event streaming flow:

```text
Producer → Kafka Topic → Consumer Group
```

### Kafka Mode

This project uses Kafka in **KRaft mode**, so ZooKeeper is not required.

```text
Kafka Broker + Kafka Controller
```

The local Docker setup runs one Kafka node with both roles:

```text
KAFKA_PROCESS_ROLES=broker,controller
```

### Topic

```text
customer_events
```

Topic configuration:

```text
Partitions: 3
Replication Factor: 1
```

### Event Types

```text
user_login
product_view
cart_add
checkout
payment_success
payment_failed
```

### Message Key

The producer uses `user_id` as the Kafka message key.

Reason:

- Events for the same user are routed to the same partition
- User-level ordering is preserved inside a partition
- Customer journey analysis becomes easier

### Consumer Group Testing

Consumer group:

```text
customer-activity-test-consumer
```

Validated behavior:

- With one consumer, all three partitions are assigned to the same consumer
- With two consumers in the same group, Kafka rebalances partition ownership
- Offsets are tracked using `CURRENT-OFFSET`, `LOG-END-OFFSET`, and `LAG`

---

## Day 2 - Databricks Medallion Architecture

### Objective

Build Databricks Bronze, Silver, and Gold layers using Delta Lake.

```text
Raw JSON → Bronze Delta → Silver Delta → Gold Delta
```

### Storage Layout

Unity Catalog Volume path used in notebooks:

```text
/Volumes/workspace/customer_analytics/data_files/
```

Folders:

```text
raw/
bronze/
silver/
gold/
checkpoints/
```

### Bronze Layer

Purpose:

- Ingest raw customer event data
- Preserve source data
- Add ingestion metadata
- Use checkpointing for streaming progress

Output:

```text
/Volumes/workspace/customer_analytics/data_files/bronze/customer_events
```

### Silver Layer

Purpose:

- Deduplicate events by `event_id`
- Validate required fields
- Keep only valid event types
- Convert event time into timestamp format
- Add processing timestamp

Output:

```text
/Volumes/workspace/customer_analytics/data_files/silver/customer_events
```

### Gold Layer

Gold tables created:

```text
daily_revenue
user_activity
event_funnel
failed_payments
```

These tables represent business-facing analytics data.

---

## Day 3 - Airflow Orchestration

Airflow DAG created:

```text
airflow/dags/customer_analytics_pipeline.py
```

DAG flow:

```text
start
  ↓
generate_sample_events
  ↓
bronze_ingestion
  ↓
silver_transformations
  ↓
gold_aggregations
  ↓
validate_pipeline
  ↓
end
```

Current DAG uses `PythonOperator` placeholders. In the production version, these tasks will be replaced with `DatabricksSubmitRunOperator` tasks.

---

## How to Run Kafka Locally

### 1. Start Kafka

```bash
cd infrastructure/docker
docker compose up -d
```

### 2. Create Kafka topic

```bash
cd ../../kafka/topics
bash create_topics.sh
```

### 3. Install dependencies

From the project root:

```bash
pip install -r requirements.txt
```

### 4. Start consumer

```bash
python kafka/consumer/test_consumer.py
```

### 5. Start producer

```bash
python kafka/producer/producer.py
```

### 6. Start second consumer to observe rebalancing

```bash
python kafka/consumer/test_consumer_2.py
```

### 7. Check consumer group offsets

```bash
docker exec kafka-kraft kafka-consumer-groups   --bootstrap-server localhost:9092   --describe   --group customer-activity-test-consumer
```

---

## Databricks Notebook Execution Order

Run notebooks in this order:

```text
00_generate_sample_events
01_bronze_ingestion
02_silver_transformations
03_gold_aggregations
```

Notebook folder:

```text
databricks/notebooks/
```

---

Add Terraform to provision Databricks resources such as schemas, volumes, jobs, and environment-specific configuration.

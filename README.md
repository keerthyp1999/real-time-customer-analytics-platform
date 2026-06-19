# Real-Time Customer Analytics Platform

This project simulates a production-style real-time data engineering pipeline using Kafka, Databricks, Delta Lake, Airflow, and Terraform.

## Day 1 Scope

- Run Kafka locally using Docker Compose in modern KRaft mode
- Create a Kafka topic named `customer_events`
- Generate realistic customer activity events using Python
- Publish events to Kafka
- Read events using a test consumer
- Understand topics, partitions, producers, consumers, offsets, and consumer groups

## Kafka Mode

This project uses Kafka in **KRaft mode**, so ZooKeeper is not required.

```text
Kafka Broker + Kafka Controller
```

The local Docker setup runs one Kafka node with both roles:

```text
KAFKA_PROCESS_ROLES=broker,controller
```

## Architecture - Day 1

```text
Python Event Producer
        ↓
Kafka Topic: customer_events
        ↓
Python Test Consumer
```

## How to Run Day 1

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

### 3. Install Python dependencies

From the project root:

```bash
pip install -r requirements.txt
```

### 4. Start producer

From the project root:

```bash
python kafka/producer/producer.py
```

### 5. Start consumer in another terminal

From the project root:

```bash
python kafka/consumer/test_consumer.py
```

### 6. Open Kafka UI

```text
http://localhost:8080
```

## Resume Line

Built a real-time Kafka event streaming pipeline using modern KRaft mode, Python producers and consumers, custom JSON event schema, topic partitioning, and local Docker-based Kafka setup.

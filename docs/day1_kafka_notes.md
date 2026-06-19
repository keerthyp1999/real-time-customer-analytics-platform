# Day 1 - Kafka Notes

## What is Kafka?

Kafka is a distributed event streaming platform used to move high-volume event data between producers and consumers.

## Project Flow

```text
Python Producer → Kafka Topic → Python Consumer
```

## Kafka Mode

This project uses Kafka in KRaft mode.

```text
Kafka Broker + Kafka Controller
```

ZooKeeper is not required.

## Topic

```text
customer_events
```

Configuration:

```text
Partitions: 3
Replication Factor: 1
```

## Producer

A producer writes events to Kafka.

In this project:

```text
kafka/producer/producer.py
```

## Consumer

A consumer reads events from Kafka.

In this project:

```text
kafka/consumer/test_consumer.py
kafka/consumer/test_consumer_2.py
```

Both consumers use the same consumer group:

```text
customer-activity-test-consumer
```

## Bootstrap Server

```text
localhost:9092
```

This is the broker address used by clients to initially connect to Kafka.

## Partition

A partition is an ordered, append-only log inside a topic.

Partitions allow Kafka to process data in parallel.

## Message Key

The producer uses:

```python
message_key = event["user_id"]
```

This keeps events for the same user in the same partition.

## Consumer Group

Within a consumer group, a partition is assigned to only one consumer at a time.

Example with three partitions and two consumers:

```text
Partition 0 → Consumer 1
Partition 1 → Consumer 2
Partition 2 → Consumer 1
```

## Offset

An offset is the position of a message within a partition.

Kafka tracks offsets for each consumer group.

Useful command:

```bash
docker exec kafka-kraft kafka-consumer-groups   --bootstrap-server localhost:9092   --describe   --group customer-activity-test-consumer
```

## Lag

```text
LAG = LOG-END-OFFSET - CURRENT-OFFSET
```

Lag tells how many messages are waiting to be consumed.

## Rebalancing

When a new consumer joins or leaves a consumer group, Kafka redistributes partition ownership. This is called rebalancing.

## Reliability Concepts Demonstrated

- Message keys
- Partitions
- Consumer groups
- Offset tracking
- Lag monitoring
- Rebalancing
